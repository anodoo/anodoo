# -*- coding: utf-8 -*-

import datetime
from datetime import time
from dateutil import relativedelta

from odoo import api, fields, models, tools, _
from odoo.osv import expression
from odoo.exceptions import AccessError
from odoo.osv import expression


class DeskTicket(models.Model):
    _inherit = 'anodoo.desk.ticket'



    team_id = fields.Many2one(
        'anodoo.desk.team',
        string='团队',
        index=True
    )

    team_assign_method = fields.Selection(related='team_id.assign_method')

    #包括选了团队，人只能在团队选）
    # user_id = fields.Many2one(
    #     domain= lambda self: [('groups_id', 'in', self.env.ref('anodoo_desk.group_desk_user').id), ('team_ids', 'in', self.team_id)]
    # )


    # use_credit_notes = fields.Boolean(related='team_id.use_credit_notes', string='Use Credit Notes')
    # use_coupons = fields.Boolean(related='team_id.use_coupons', string='Use Coupons')
    # use_product_returns = fields.Boolean(related='team_id.use_product_returns', string='Use Returns')
    # use_product_repairs = fields.Boolean(related='team_id.use_product_repairs', string='Use Repairs')

    @api.model
    def default_get(self, fields):
        result = super(DeskTicket, self).default_get(fields)

        if 'team_id' in fields or 'user_id' in fields:
            if 'team_id' not in result:
                team_id = self.env['anodoo.desk.team'].search([('member_user_ids', 'in', self.env.uid)], limit=1).id
                if not team_id:
                    team_id = self.env['anodoo.desk.team'].search([], limit=1).id

                if team_id:
                    result['team_id'] = team_id

        #父类默认user_id为当前用户。这里重写之，通过团队的规则来设置user_id
        if 'user_id' in fields and result.get('team_id'):
            team = self.env['anodoo.desk.team'].browse(result['team_id'])
            result['user_id'] = team._determine_user_to_assign()[team.id].id

        return result

    @api.onchange('team_id')
    def _onchange_team_id(self):
        if self.team_id:
            #改进：即使已经有了user_id,也要进一步去判断这个user_id是否是属于这个team_id的。
            #不过这样性能慢一点
            self.user_id = self.team_id._determine_user_to_assign(self.user_id)[self.team_id.id]
        else:
            self.user_id = False

    def assign_ticket_to_self(self):
        self.ensure_one()

        team_id = self.env['anodoo.desk.team'].search(
            [('member_user_ids', 'in', self.env.uid)], limit=1).id
        if team_id:
            self.team_id = team_id
            self.user_id = self.env.user
        else:
            pass
            #这里告警给用户

    @api.model_create_multi
    def create(self, list_value):
        # determine user_id if not given. Done in batch.
        teams = self.env['anodoo.desk.team'].browse([vals['team_id'] for vals in list_value if vals.get('team_id')])
        team_default_map = dict.fromkeys(teams.ids, dict())
        for team in teams:
            team_default_map[team.id] = {
                'user_id': team._determine_user_to_assign()[team.id].id
            }



        for vals in list_value:
            if vals.get('team_id'):
                team_default = team_default_map[vals['team_id']]

                # Note: this will break the randomly distributed user assignment. Indeed, it will be too difficult to
                # equally assigned user when creating ticket in batch, as it requires to search after the last assigned
                # after every ticket creation, which is not very performant. We decided to not cover this user case.
                if 'user_id' not in vals:
                    vals['user_id'] = team_default['user_id']
                if vals.get('user_id'):  # if a user is finally assigned, force ticket assign_date and reset assign_hours
                    vals['assign_date'] = fields.Datetime.now()
                    vals['assign_hours'] = 0


        # context: no_log, because subtype already handle this
        tickets = super(DeskTicket, self).create(list_value)

        return tickets

    #重写，优先顺序是个人，team，company中取工作时间表
    def _get_calendar_id(self, ticket):
        if ticket.user_id and ticket.user_id.resource_calendar_id:
            return ticket.user_id.resource_calendar_id
        elif ticket.team_id and ticket.team_id.resource_calendar_id:
            return ticket.team_id.resource_calendar_id
        else:
            return ticket.company_id.resource_calendar_id

    #这里有team_id，看怎么改
    def _notify_get_reply_to(self, default=None, records=None, company=None, doc_names=None):
        """ Override to set alias of tickets to their team if any. """
        aliases = self.mapped('team_id').sudo()._notify_get_reply_to(default=default, records=None, company=company, doc_names=None)
        res = {ticket.id: aliases.get(ticket.team_id.id) for ticket in self}
        leftover = self.filtered(lambda rec: not rec.team_id)
        if leftover:
            res.update(super(DeskTicket, leftover)._notify_get_reply_to(default=default, records=None, company=company, doc_names=doc_names))
        return res