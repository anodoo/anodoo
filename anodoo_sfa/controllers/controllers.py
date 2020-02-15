# -*- coding: utf-8 -*-
from odoo import http

# class AnodooSfa(http.Controller):
#     @http.route('/anodoo_sfa/anodoo_sfa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_sfa/anodoo_sfa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_sfa.listing', {
#             'root': '/anodoo_sfa/anodoo_sfa',
#             'objects': http.request.env['anodoo_sfa.anodoo_sfa'].search([]),
#         })

#     @http.route('/anodoo_sfa/anodoo_sfa/objects/<model("anodoo_sfa.anodoo_sfa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_sfa.object', {
#             'object': obj
#         })