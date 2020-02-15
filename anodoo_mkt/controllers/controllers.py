# -*- coding: utf-8 -*-
from odoo import http

# class AnodooMkt(http.Controller):
#     @http.route('/anodoo_mkt/anodoo_mkt/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_mkt/anodoo_mkt/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_mkt.listing', {
#             'root': '/anodoo_mkt/anodoo_mkt',
#             'objects': http.request.env['anodoo_mkt.anodoo_mkt'].search([]),
#         })

#     @http.route('/anodoo_mkt/anodoo_mkt/objects/<model("anodoo_mkt.anodoo_mkt"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_mkt.object', {
#             'object': obj
#         })