# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class anodoo_base(models.Model):
#     _name = 'anodoo_base.anodoo_base'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class IrTranslation(models.Model):
    _inherit = "ir.translation"
    
    anodoo = fields.Boolean('Anodoo标记', default=False)
    
#Anodoo中对res.partner的基类定义
class Parnter(models.Model):
    _inherit = 'res.partner'
    
    partner_type = fields.Char('扩展类型', default='contact', help='Anodoo按照Odoo设计，用来实现contact,customer, dealer等')
    
    #重写父类，名称还是使用本身的名称
    def _get_name(self):
        return self.name

    