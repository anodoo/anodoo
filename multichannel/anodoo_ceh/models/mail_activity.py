# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EngageActivityType(models.Model):
    
    _inherit = 'mail.activity.type'
    
    engage_channel_id = fields.Many2one('anodoo.engage.channel', string='交互渠道')
    
    online = fields.Selection([('online', '线上'), ('offline', '线下'), ('on_and_off', '线上和线下')], required=True, string='线上或线下')
    
    cancreate = fields.Boolean('是否可创建', default=False)
    
class EngageActivity(models.Model):
    
    _inherit = 'mail.activity'
    
    customer_id = fields.Many2one('res.partner', string='客户', index=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", help="")