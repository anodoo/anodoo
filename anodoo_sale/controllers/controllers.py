# -*- coding: utf-8 -*-
from odoo import http

# class AnodooSale(http.Controller):
#     @http.route('/anodoo_sale/anodoo_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_sale/anodoo_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_sale.listing', {
#             'root': '/anodoo_sale/anodoo_sale',
#             'objects': http.request.env['anodoo_sale.anodoo_sale'].search([]),
#         })

#     @http.route('/anodoo_sale/anodoo_sale/objects/<model("anodoo_sale.anodoo_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_sale.object', {
#             'object': obj
#         })