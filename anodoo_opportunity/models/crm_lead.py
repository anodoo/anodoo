# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Opportunity(models.Model):
    _inherit = 'crm.lead'

    lead_id = fields.Many2one('crm.lead', string='线索', ondelete='restrict')

    opportunity_relation_ids = fields.One2many('anodoo.opportunity.relation', 'opportunity_id', string='商机与商机关系')

    team_name = fields.Char('团队名称', related='team_id.name')
    # team_description = fields.Text('团队描述', related='team_id.description')

    def _default_opportunity_lifetime_id(self):

        type = self._context.get('default_type')
        if not type:
            type = self.type

        if type == 'opportunity':
            return self.env['anodoo.opportunity.lifetime'].search([], limit=1)

        return None

    opportunity_lifetime_id = fields.Many2one('anodoo.opportunity.lifetime', string='生命周期', help='商机的生命周期定义',
                                       default=_default_opportunity_lifetime_id)

    is_opportunity_qualify = fields.Boolean('是否认定阶段', related='stage_id.is_qualify', default=False)

    opportunity_qualify_lost_reason = fields.Many2one('anodoo.opportunity.qualify.lost.reason', string='商机认定失败原因')


    def _stage_find(self, team_id=False, domain=None, order='sequence'):
        lifetime = self._default_opportunity_lifetime_id()
        if lifetime:
            search_domain = [('opportunity_lifetime_id', '=', lifetime.id)]
        else:
            search_domain = []

        if domain:
            search_domain += list(domain)

        return super()._stage_find(team_id=team_id, domain=search_domain, order=order)

    def action_set_opportunity_qualify_lost(self, **additional_values):
        """ Lost semantic: probability = 0 or active = False """
        result = self.write({'active': False, 'probability': 0, 'automated_probability': 0, **additional_values})
        self._rebuild_pls_frequency_table_threshold()
        return result

    def qualify_opportunity_success(self):
        pass