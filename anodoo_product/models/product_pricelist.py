# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pricelist(models.Model):
    _inherit = "product.pricelist"
    
    date_start = fields.Date('开始时间', help="价格表的有效开始时间,适用于所有价格项")
    date_end = fields.Date('结束时间', help="价格表的有效结束时间,适用于所有价格项")
    
    
    #sale_territory_ids = fields.Many2many('anodoo.sale.territory', string='销售区域')
    
    customer_ids = fields.Many2many('res.partner', compute='_compute_customer_ids', store=False)

    def _compute_customer_ids(self):
        self.customer_ids = self.env['res.partner'].browse([1,2,3])
    

class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"
    
    date_start = fields.Date('开始时间', default=lambda self: self.pricelist_id.date_start)
    date_end = fields.Date('结束时间', default=lambda self: self.pricelist_id.date_end)
    
    