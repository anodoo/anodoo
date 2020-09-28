# -*- coding: utf-8 -*-

from odoo import api, fields, models


class LeadQualifyLost(models.TransientModel):
    _name = 'anodoo.lead.qualify.lost'
    _description = '设置认定失败理由的向导'
    
    is_for = fields.Char('适用范围')
    
    lost_reason_id = fields.Many2one('anodoo.lead.qualify.lost.reason', string='认定失败理由', domain='[("is_for", "=", is_for)]')

    def action_lost_reason_apply(self):
        leads = self.env['crm.lead'].browse(self.env.context.get('active_ids'))
        return leads.action_set_qualify_lost(qualify_lost_reason=self.lost_reason_id.id)
