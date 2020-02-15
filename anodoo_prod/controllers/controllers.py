# -*- coding: utf-8 -*-
from odoo import http

# class AnodooProd(http.Controller):
#     @http.route('/anodoo_prod/anodoo_prod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_prod/anodoo_prod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_prod.listing', {
#             'root': '/anodoo_prod/anodoo_prod',
#             'objects': http.request.env['anodoo_prod.anodoo_prod'].search([]),
#         })

#     @http.route('/anodoo_prod/anodoo_prod/objects/<model("anodoo_prod.anodoo_prod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_prod.object', {
#             'object': obj
#         })