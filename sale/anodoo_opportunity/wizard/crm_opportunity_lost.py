# -*- coding: utf-8 -*-

from odoo import api, fields, models


class OpportunityQualifyLost(models.TransientModel):
    _name = 'anodoo.opportunity.qualify.lost'
    _description = '设置认定失败理由的向导'

    
    lost_reason_id = fields.Many2one('anodoo.opportunity.qualify.lost.reason', string='认定失败理由')

    def action_lost_reason_apply(self):
        opportunitys = self.env['crm.lead'].browse(self.env.context.get('active_ids'))
        return opportunitys.action_set_opportunity_qualify_lost(opportunity_qualify_lost_reason=self.lost_reason_id.id)
