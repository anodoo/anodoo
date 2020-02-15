# -*- coding: utf-8 -*-
from odoo import http

# class AnodooProj(http.Controller):
#     @http.route('/anodoo_proj/anodoo_proj/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_proj/anodoo_proj/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_proj.listing', {
#             'root': '/anodoo_proj/anodoo_proj',
#             'objects': http.request.env['anodoo_proj.anodoo_proj'].search([]),
#         })

#     @http.route('/anodoo_proj/anodoo_proj/objects/<model("anodoo_proj.anodoo_proj"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_proj.object', {
#             'object': obj
#         })