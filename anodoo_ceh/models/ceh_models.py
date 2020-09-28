# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class anodoo_engage(models.Model):
#     _name = 'anodoo_engage.anodoo_engage'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class EngageChannel(models.Model):
    _name = 'anodoo.engage.channel'
    _description = '客户交互渠道'
    _order = "sequence"
        
    code = fields.Char('代码', required=True)
    name = fields.Char('名称', required=True, translate=False)
    description = fields.Text('描述', translate=False)
    
    online = fields.Selection([('online', '线上'), ('offline', '线下'), ('on_and_off', '线上和线下')], required=True, string='线上或线下')
    type = fields.Selection([('intype', '自有交互渠道'), ('outtype', '第三方交互渠道')], required=True, string='是否自有交互渠道' )
    sequence = fields.Integer('序号')


    
    
    
    