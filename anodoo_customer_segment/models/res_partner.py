# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Customer(models.Model):

    _inherit = 'res.partner'

    customer_label_ids = fields.Many2many('anodoo.customer.label', 'anodoo_customer_label_ref', 'customer_id',
                                          'label_id', string='客户标签', help='客户当前的所有标签')
    customer_label_auto_ids = fields.Many2many('anodoo.customer.label', 'anodoo_customer_label_auto_ref', 'customer_id',
                                               'label_id', string='客户标签(自动)', help='客户自动标签')

