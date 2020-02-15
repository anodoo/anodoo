# -*- coding: utf-8 -*-
from odoo import http

# class AnodooEngage(http.Controller):
#     @http.route('/anodoo_engage/anodoo_engage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_engage/anodoo_engage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_engage.listing', {
#             'root': '/anodoo_engage/anodoo_engage',
#             'objects': http.request.env['anodoo_engage.anodoo_engage'].search([]),
#         })

#     @http.route('/anodoo_engage/anodoo_engage/objects/<model("anodoo_engage.anodoo_engage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_engage.object', {
#             'object': obj
#         })