# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductCategory(models.Model):
    _inherit = "product.category"
    
    #放在anodoo sale模块
    #user_id = fields.Many2one('res.users', string='销售负责人')
    
    #sale_territory_ids = fields.Many2many('anodoo.sale.territory', string='销售区域')

class ProductTemplate(models.Model):

    _inherit = 'product.template'
    
    type = fields.Selection(selection_add=[('saas', 'SaaS产品'), ('member', '会员产品'), ('software', '软件产品'), ('digit', '数字产品')])

    #放在anodoo sale模块
    #user_id = fields.Many2one('res.users', string='销售负责人')
    
    #sale_territory_ids = fields.Many2many('anodoo.sale.territory', string='销售区域')