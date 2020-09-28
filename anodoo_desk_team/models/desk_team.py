# -*- coding: utf-8 -*-

import datetime
from dateutil import relativedelta
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression


class DeskTeam(models.Model):
    _name = 'anodoo.desk.team'
    _description = '工单客服团队'
    _inherit = ['anodoo.team']

    def _default_domain_member_ids(self):
        return [('groups_id', 'in', self.env.ref('anodoo_desk.group_desk_user').id)]

    member_user_ids = fields.Many2many(domain=lambda self: self._default_domain_member_ids())

    assign_method = fields.Selection(
        [
            ('manual', '手动分配'),
        ],
        string='工单分配方式',
        default='manual',
        required=True
    )

    unassigned_ticket_count = fields.Integer(string='Unassigned Tickets', compute='_compute_unassigned_ticket_count')

    ticket_ids = fields.One2many('anodoo.desk.ticket', 'team_id', string='工单')

    #一个人属于多个team时，可以获取默认的team
    @api.model
    @api.returns('self', lambda value: value.id if value else False)
    def _get_default_team_id(self, user_id=None, domain=None):
        if not user_id:
            user_id = self.env.uid

        DeskTeam = self.env['anodoo.desk.team']

        team_id = DeskTeam.search([
            '|', ('user_id', '=', user_id), ('member_ids', '=', user_id),
            '|', ('company_id', '=', False), ('company_id', '=', self.env.company.id)
        ], limit=1)
        if not team_id and 'default_team_id' in self.env.context:
            team_id = DeskTeam.browse(self.env.context.get('default_team_id'))
        if not team_id:
            team_domain = domain or []
            default_team_id = DeskTeam.search(team_domain, limit=1)
            return default_team_id or DeskTeam
        return team_id

    def _compute_unassigned_ticket_count(self):
        ticket_data = self.env['anodoo.desk.ticket'].read_group([('user_id', '=', False), ('team_id', 'in', self.ids), ('stage_id.is_close', '!=', True)], ['team_id'], ['team_id'])
        mapped_data = dict((data['team_id'][0], data['team_id_count']) for data in ticket_data)
        for team in self:
            team.unassigned_ticket_count = mapped_data.get(team.id, 0)

    @api.onchange('member_user_ids')
    def _onchange_member_user_ids(self):
        if not self.member_user_ids:
            self.assign_method = 'manual'



    @api.constrains('assign_method', 'member_user_ids')
    def _check_member_assignation(self):
        if not self.member_user_ids and self.assign_method != 'manual':
            raise ValidationError(_("You must have team members assigned to change the assignation method."))



    def _determine_user_to_assign(self, default_user_id=None):
        """ Get a dict with the user (per team) that should be assign to the nearly created ticket according to the team policy
            :returns a mapping of team identifier with the "to assign" user (maybe an empty record).
            :rtype : dict (key=team_id, value=record of res.users)
        """
        result = dict.fromkeys(self.ids, self.env['res.users'])
        for team in self:
            member_user_ids = sorted(team.member_user_ids.ids)
            if member_user_ids:
                if not team.assign_method or team.assign_method == 'manual':
                    user_id = 0
                    if default_user_id and default_user_id in member_user_ids:
                        user_id = default_user_id
                    elif self.env.uid in member_user_ids:
                        user_id = self.env.uid
                    else:
                        user_id = member_user_ids[0]

                    if user_id:
                        result[team.id] = self.env['res.users'].browse(user_id)

        return result



