# -*- coding: utf-8 -*-
from odoo import http

# class AnodooCust(http.Controller):
#     @http.route('/anodoo_cust/anodoo_cust/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_cust/anodoo_cust/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_cust.listing', {
#             'root': '/anodoo_cust/anodoo_cust',
#             'objects': http.request.env['anodoo_cust.anodoo_cust'].search([]),
#         })

#     @http.route('/anodoo_cust/anodoo_cust/objects/<model("anodoo_cust.anodoo_cust"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_cust.object', {
#             'object': obj
#         })