# -*- coding: utf-8 -*-
from odoo import http

# class AnodooBase(http.Controller):
#     @http.route('/anodoo_base/anodoo_base/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_base/anodoo_base/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_base.listing', {
#             'root': '/anodoo_base/anodoo_base',
#             'objects': http.request.env['anodoo_base.anodoo_base'].search([]),
#         })

#     @http.route('/anodoo_base/anodoo_base/objects/<model("anodoo_base.anodoo_base"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_base.object', {
#             'object': obj
#         })