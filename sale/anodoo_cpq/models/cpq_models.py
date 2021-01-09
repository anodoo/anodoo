# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderTemplate(models.Model):
    _order = "sequence"
    _inherit = ['sale.order.template']

    sequence = fields.Integer('排序', default=10)

    description = fields.Text('模板使用备注')