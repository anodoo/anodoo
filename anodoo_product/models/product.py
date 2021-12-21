# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductCategory(models.Model):
    _inherit = "product.category"

    code = fields.Char('编码')

    sequence = fields.Integer('排序', default=10)

    description = fields.Text('说明')

    # 放在anodoo sale模块
    # user_id = fields.Many2one('res.users', string='销售负责人')

    # sale_territory_ids = fields.Many2many('anodoo.sale.territory', string='销售区域')