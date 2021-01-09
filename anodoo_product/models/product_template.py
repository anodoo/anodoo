# -*- coding: utf-8 -*-

from odoo import models, fields, api



class ProductTemplate(models.Model):

    _inherit = 'product.template'

    #新增类型需要在不同的模块扩展。
    # type = fields.Selection(selection_add=[('saas', 'SaaS产品'), ('member', '会员产品'), ('software', '软件产品'), ('digit', '数字产品')]
    # , ondelete="set default“)

    #放在anodoo sale模块
    #user_id = fields.Many2one('res.users', string='销售负责人')
    
    #sale_territory_ids = fields.Many2many('anodoo.sale.territory', string='销售区域')