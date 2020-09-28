# -*- coding: utf-8 -*-

from dateutil import relativedelta

from odoo import api, fields, models, tools, _
from odoo.osv import expression
from odoo.exceptions import AccessError
from odoo.osv import expression

TICKET_PRIORITY = [
    ('0', ''),
    ('1', '低'),
    ('2', '高'),
    ('3', '紧急'),
]


class DeskTicket(models.Model):
    _name = 'anodoo.desk.ticket'
    _description = '工单'
    _order = 'priority desc, id desc'
    _inherit = ['mail.thread.cc', 'mail.activity.mixin']
    #_inherit = ['portal.mixin', 'mail.thread.cc', 'utm.mixin', 'rating.mixin', 'mail.activity.mixin']

    name = fields.Char(string='标题', required=True, index=True)

    description = fields.Text(string='描述')

    active = fields.Boolean(default=True)

    type_id = fields.Many2one('anodoo.desk.type', string="类型")

    channel_id = fields.Many2one('anodoo.desk.channel', string="来源")

    tag_ids = fields.Many2many('anodoo.desk.tag', string='标签')

    user_id = fields.Many2one(
        'res.users',
        string='负责人',
        tracking=True,
        domain=lambda self: [('groups_id', 'in', self.env.ref('anodoo_desk.group_desk_user').id)]
    )

    company_id = fields.Many2one(related='user_id.company_id', string='公司', store=True, readonly=True)

    color = fields.Integer(string='颜色索引')

    kanban_state = fields.Selection([
        ('normal', 'Grey'),
        ('done', 'Green'),
        ('blocked', 'Red')],
        string='看板状态',
        default='normal',
        required=True
    )

    kanban_state_label = fields.Char(compute='_compute_kanban_state_label', string='Column Status', tracking=True)

    legend_blocked = fields.Char(related='stage_id.legend_blocked', string='Kanban Blocked Explanation', readonly=True, related_sudo=False)
    legend_done = fields.Char(related='stage_id.legend_done', string='Kanban Valid Explanation', readonly=True, related_sudo=False)
    legend_normal = fields.Char(related='stage_id.legend_normal', string='Kanban Ongoing Explanation', readonly=True, related_sudo=False)


    attachment_number = fields.Integer(compute='_compute_attachment_number', string="Number of Attachments")

    is_self_assigned = fields.Boolean("是否分配自己", compute='_compute_is_self_assigned', help='用来控制是否分配给自己的按钮')

    priority = fields.Selection(TICKET_PRIORITY, string='优先级', default='0')

    stage_id = fields.Many2one(
        'anodoo.desk.stage',
        string='阶段',
        tracking=True,
        group_expand='_read_group_stage_ids',
        copy=False
    )

    date_last_stage_update = fields.Datetime("阶段最后更新时间", copy=False, readonly=True)

    # next 4 fields are computed in write (or create)
    assign_date = fields.Datetime("首次分配时间")
    assign_hours = fields.Integer("分配花费时间(小时)", compute='_compute_assign_hours', store=True, help='已经分配工单，分配时间到创建时间的间隔小时数')
    close_date = fields.Datetime("关闭时间")
    close_hours = fields.Integer("关闭花费时间(小时)", compute='_compute_close_hours', store=True, help='已经关闭工单，关闭时间到创建时间的间隔小时数')
    open_hours = fields.Integer("打开时间(小时)", compute='_compute_open_hours', search='_search_open_hours', help='处在打开状态的工单时间，如果已关闭，则是关闭花费时间')

    #以下可客户相关

    partner_id = fields.Many2one('res.partner', string='客户')

    #没看到在哪里用
    partner_ticket_count = fields.Integer('Number of closed tickets from the same partner',
                                          compute='_compute_partner_ticket_count')

    # Used to submit tickets from a contact form
    partner_name = fields.Char(string='客户名称')

    partner_email = fields.Char(string='客户邮箱')

    # Used in message_get_default_recipients, so if no partner is created, email is sent anyway
    email = fields.Char(related='partner_email', string='Email on Customer', readonly=False)

    @api.model
    def default_get(self, fields):
        result = super(DeskTicket, self).default_get(fields)

        if 'user_id' in fields and 'user_id' not in result:  # if no user given, deduce it from the team
            result['user_id'] = self.env.uid

        if 'stage_id' in fields and 'stage_id' not in result:
            stage = self._get_default_stage_id()
            if stage:
                result['stage_id'] = stage.id

        return result



    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        # write the domain
        # - ('id', 'in', stages.ids): add columns that should be present
        # - OR ('team_ids', '=', team_id) if team_id: add team columns
        search_domain = [('id', 'in', stages.ids)]

        # 再考虑要不要这个
        # if self.env.context.get('default_team_id'):
        #     search_domain = ['|', ('team_ids', 'in', self.env.context['default_team_id'])] + search_domain

        return stages.search(search_domain, order=order)

    @api.depends('stage_id', 'kanban_state')
    def _compute_kanban_state_label(self):
        for task in self:
            if task.kanban_state == 'normal':
                task.kanban_state_label = task.legend_normal
            elif task.kanban_state == 'blocked':
                task.kanban_state_label = task.legend_blocked
            else:
                task.kanban_state_label = task.legend_done



    def _compute_attachment_number(self):
        read_group_res = self.env['ir.attachment'].read_group(
            [('res_model', '=', 'anodoo.desk.ticket'), ('res_id', 'in', self.ids)],
            ['res_id'], ['res_id'])
        attach_data = { res['res_id']: res['res_id_count'] for res in read_group_res }
        for record in self:
            record.attachment_number = attach_data.get(record.id, 0)



    @api.depends('user_id')
    def _compute_is_self_assigned(self):
        for ticket in self:
            ticket.is_self_assigned = self.env.user == ticket.user_id

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.partner_name = self.partner_id.name
            self.partner_email = self.partner_id.email

    @api.depends('partner_id')
    def _compute_partner_ticket_count(self):
        data = self.env['anodoo.desk.ticket'].read_group([
            ('partner_id', 'in', self.mapped('partner_id').ids),
            ('stage_id.is_close', '=', False)
        ], ['partner_id'], ['partner_id'], lazy=False)
        ticket_per_partner_map = dict((item['partner_id'][0], item['__count']) for item in data)
        for ticket in self:
            ticket.partner_ticket_count = ticket_per_partner_map.get(ticket.partner_id.id, 0)


    def _get_calendar_id(self, ticket):
        if ticket.user_id and ticket.user_id.resource_calendar_id:
            return ticket.user_id.resource_calendar_id
        else:
            return ticket.company_id.resource_calendar_id




    # 重写，根据team的日历来计算
    @api.depends('assign_date')
    def _compute_assign_hours(self):
        for ticket in self:
            create_date = fields.Datetime.from_string(ticket.create_date)
            if create_date and ticket.assign_date:
                duration_data = self._get_calendar_id(ticket).get_work_duration_data(create_date,
                                                                                           fields.Datetime.from_string(
                                                                                               ticket.assign_date),
                                                                                           compute_leaves=True)
                ticket.assign_hours = duration_data['hours']
            else:
                ticket.assign_hours = False

    # 重写，根据team的日历来计算
    @api.depends('create_date', 'close_date')
    def _compute_close_hours(self):
        for ticket in self:
            create_date = fields.Datetime.from_string(ticket.create_date)
            if create_date and ticket.close_date:
                duration_data = self._get_calendar_id(ticket).get_work_duration_data(create_date,
                                                                                           fields.Datetime.from_string(
                                                                                               ticket.close_date),
                                                                                           compute_leaves=True)
                ticket.close_hours = duration_data['hours']
            else:
                ticket.close_hours = False



    @api.depends('close_hours')
    def _compute_open_hours(self):
        for ticket in self:
            create_date = fields.Datetime.from_string(ticket.create_date)
            if create_date:
                if ticket.close_date:
                    total_interval_time = (ticket.close_date - create_date).total_seconds()
                else:
                    total_interval_time = (fields.Datetime.now() - create_date).total_seconds()
                ticket.open_hours = total_interval_time / 3600
            else:
                ticket.open_hours = 0

    @api.model
    def _search_open_hours(self, operator, value):
        dt = fields.Datetime.now() - relativedelta.relativedelta(hours=value)

        d1, d2 = False, False
        if operator in ['<', '<=', '>', '>=']:
            d1 = ['&', ('close_date', '=', False), ('create_date', expression.TERM_OPERATORS_NEGATION[operator], dt)]
            d2 = ['&', ('close_date', '!=', False), ('close_hours', operator, value)]
        elif operator in ['=', '!=']:
            subdomain = ['&', ('create_date', '>=', dt.replace(minute=0, second=0, microsecond=0)), ('create_date', '<=', dt.replace(minute=59, second=59, microsecond=99))]
            if operator in expression.NEGATIVE_TERM_OPERATORS:
                subdomain = expression.distribute_not(subdomain)
            d1 = expression.AND([[('close_date', '=', False)], subdomain])
            d2 = ['&', ('close_date', '!=', False), ('close_hours', operator, value)]
        return expression.OR([d1, d2])

    # ------------------------------------------------------------
    # ORM overrides
    # ------------------------------------------------------------

    def name_get(self):
        result = []
        for ticket in self:
            result.append((ticket.id, "%s (#%d)" % (ticket.name, ticket._origin.id)))
        return result

    @api.model_create_multi
    def create(self, list_value):
        now = fields.Datetime.now()

        # Manually create a partner now since 'generate_recipients' doesn't keep the name. This is
        # to avoid intrusive changes in the 'mail' module
        for vals in list_value:
            if 'partner_name' in vals and 'partner_email' in vals and 'partner_id' not in vals:
                try:
                    vals['partner_id'] = self.env['res.partner'].find_or_create(
                        tools.formataddr((vals['partner_name'], vals['partner_email']))
                    )
                except UnicodeEncodeError:
                    # 'formataddr' doesn't support non-ascii characters in email. Therefore, we fall
                    # back on a simple partner creation.
                    vals['partner_id'] = self.env['res.partner'].create({
                        'name': vals['partner_name'],
                        'email': vals['partner_email'],
                    }).id

        # determine partner email for ticket with partner but no email given
        partners = self.env['res.partner'].browse([vals['partner_id'] for vals in list_value if
                                                   'partner_id' in vals and vals.get(
                                                       'partner_id') and 'partner_email' not in vals])
        partner_email_map = {partner.id: partner.email for partner in partners}
        partner_name_map = {partner.id: partner.name for partner in partners}

        for vals in list_value:

            # set partner email if in map of not given
            if vals.get('partner_id') in partner_email_map:
                vals['partner_email'] = partner_email_map.get(vals['partner_id'])
            # set partner name if in map of not given
            if vals.get('partner_id') in partner_name_map:
                vals['partner_name'] = partner_name_map.get(vals['partner_id'])

        for vals in list_value:
            if vals.get('user_id'):
                vals['assign_date'] = fields.Datetime.now()
                vals['assign_hours'] = 0

            if vals.get('stage_id'):
                vals['date_last_stage_update'] = now

                #新增即关闭的场景
                if self.env['anodoo.desk.stage'].browse(vals.get('stage_id')).is_close:
                    vals['close_date'] = now


        tickets = super(DeskTicket, self).create(list_value)

        # make customer follower
        for ticket in tickets:
            if ticket.partner_id:
                ticket.message_subscribe(partner_ids=ticket.partner_id.ids)

        return tickets

    def write(self, vals):
        #更新分配时间，关闭时间
        assigned_tickets = closed_tickets = self.browse()
        if vals.get('user_id'):
            assigned_tickets = self.filtered(lambda ticket: not ticket.assign_date)

        if vals.get('stage_id'):
            if self.env['anodoo.desk.stage'].browse(vals.get('stage_id')).is_close:
                closed_tickets = self.filtered(lambda ticket: not ticket.close_date)

        now = fields.Datetime.now()

        # update last stage date when changing stage
        if 'stage_id' in vals:
            vals['date_last_stage_update'] = now

        res = super(DeskTicket, self - assigned_tickets - closed_tickets).write(vals)

        res &= super(DeskTicket, assigned_tickets - closed_tickets).write(dict(vals, **{
            'assign_date': now,
        }))
        res &= super(DeskTicket, closed_tickets - assigned_tickets).write(dict(vals, **{
            'close_date': now,
        }))
        res &= super(DeskTicket, assigned_tickets & closed_tickets).write(dict(vals, **{
            'assign_date': now,
            'close_date': now,
        }))

        if vals.get('partner_id'):
            self.message_subscribe([vals['partner_id']])


        return res

    # ------------------------------------------------------------
    # Actions and Business methods
    # ------------------------------------------------------------



    def assign_ticket_to_self(self):
        self.ensure_one()
        self.user_id = self.env.user

    def open_customer_tickets(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Customer Tickets'),
            'res_model': 'anodoo.desk.ticket',
            'view_mode': 'kanban,tree,form,pivot,graph',
            'context': {'search_default_is_open': True, 'search_default_partner_id': self.partner_id.id}
        }

    def action_get_attachment_tree_view(self):
        attachment_action = self.env.ref('base.action_attachment')
        action = attachment_action.read()[0]
        action['domain'] = str(['&', ('res_model', '=', self._name), ('res_id', 'in', self.ids)])
        return action

    # ------------------------------------------------------------
    # Messaging API
    # ------------------------------------------------------------

    #DVE FIXME: if partner gets created when sending the message it should be set as partner_id of the ticket.
    def _message_get_suggested_recipients(self):
        recipients = super(DeskTicket, self)._message_get_suggested_recipients()
        try:
            for ticket in self:
                if ticket.partner_id and ticket.partner_id.email:
                    ticket._message_add_suggested_recipient(recipients, partner=ticket.partner_id, reason=_('Customer'))
                elif ticket.partner_email:
                    ticket._message_add_suggested_recipient(recipients, email=ticket.partner_email, reason=_('Customer Email'))
        except AccessError:  # no read access rights -> just ignore suggested recipients because this implies modifying followers
            pass
        return recipients



    def _ticket_email_split(self, msg):
        email_list = tools.email_split((msg.get('to') or '') + ',' + (msg.get('cc') or ''))
        # check left-part is not already an alias
        return [
            x for x in email_list
            if x.split('@')[0] not in self.mapped('team_id.alias_name')
        ]

    @api.model
    def message_new(self, msg, custom_values=None):
        values = dict(custom_values or {}, partner_email=msg.get('from'), partner_id=msg.get('author_id'))
        ticket = super(DeskTicket, self).message_new(msg, custom_values=values)
        partner_ids = [x.id for x in self.env['mail.thread']._mail_find_partner_from_emails(self._ticket_email_split(msg), records=ticket) if x]
        customer_ids = [p.id for p in self.env['mail.thread']._mail_find_partner_from_emails(tools.email_split(values['partner_email']), records=ticket) if p]
        partner_ids += customer_ids
        if customer_ids and not values.get('partner_id'):
            ticket.partner_id = customer_ids[0]
        if partner_ids:
            ticket.message_subscribe(partner_ids)
        return ticket

    def message_update(self, msg, update_vals=None):
        partner_ids = [x.id for x in self.env['mail.thread']._mail_find_partner_from_emails(self._ticket_email_split(msg), records=self) if x]
        if partner_ids:
            self.message_subscribe(partner_ids)
        return super(DeskTicket, self).message_update(msg, update_vals=update_vals)


    def _message_post_after_hook(self, message, msg_vals):
        if self.partner_email and self.partner_id and not self.partner_id.email:
            self.partner_id.email = self.partner_email

        if self.partner_email and not self.partner_id:
            # we consider that posting a message with a specified recipient (not a follower, a specific one)
            # on a document without customer means that it was created through the chatter using
            # suggested recipients. This heuristic allows to avoid ugly hacks in JS.
            new_partner = message.partner_ids.filtered(lambda partner: partner.email == self.partner_email)
            if new_partner:
                self.search([
                    ('partner_id', '=', False),
                    ('partner_email', '=', new_partner.email),
                    ('stage_id.fold', '=', False)]).write({'partner_id': new_partner.id})
        return super(DeskTicket, self)._message_post_after_hook(message, msg_vals)



    def _track_template(self, changes):
        res = super(DeskTicket, self)._track_template(changes)
        ticket = self[0]
        if 'stage_id' in changes and ticket.stage_id.template_id:
            res['stage_id'] = (ticket.stage_id.template_id, {
                'auto_delete_message': True,
                'subtype_id': self.env['ir.model.data'].xmlid_to_res_id('mail.mt_note'),
                'email_layout_xmlid': 'mail.mail_notification_light'
            }
        )
        return res

    def _creation_subtype(self):
        return self.env.ref('anodoo_desk.mt_ticket_new')

    def _track_subtype(self, init_values):
        self.ensure_one()
        if 'stage_id' in init_values:
            return self.env.ref('anodoo_desk.mt_ticket_stage')
        return super(DeskTicket, self)._track_subtype(init_values)

    def _notify_get_groups(self):
        """ Handle desk users and managers recipients that can assign
        tickets directly from notification emails. Also give access button
        to portal and portal customers. If they are notified they should
        probably have access to the document. """
        groups = super(DeskTicket, self)._notify_get_groups()

        self.ensure_one()
        for group_name, group_method, group_data in groups:
            if group_name != 'customer':
                group_data['has_button_access'] = True

        if self.user_id:
            return groups

        take_action = self._notify_get_action_link('assign')
        desk_actions = [{'url': take_action, 'title': _('Assign to me')}]
        desk_user_group_id = self.env.ref('anodoo_desk.group_desk_user').id
        new_groups = [(
            'anodoo_desk.group_desk_user',
            lambda pdata: pdata['type'] == 'user' and desk_user_group_id in pdata['groups'],
            {'actions': desk_actions}
        )]
        return new_groups + groups

    def _get_default_stage_id(self):
        stages = self.env['anodoo.desk.stage'].search([], limit=1, order='sequence')
        if len(stages) > 0:
            return stages[0]

        return None

