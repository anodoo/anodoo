# -*- coding: utf-8 -*-
from odoo import http

# class AnodooMktauto(http.Controller):
#     @http.route('/anodoo_mktauto/anodoo_mktauto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_mktauto/anodoo_mktauto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_mktauto.listing', {
#             'root': '/anodoo_mktauto/anodoo_mktauto',
#             'objects': http.request.env['anodoo_mktauto.anodoo_mktauto'].search([]),
#         })

#     @http.route('/anodoo_mktauto/anodoo_mktauto/objects/<model("anodoo_mktauto.anodoo_mktauto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_mktauto.object', {
#             'object': obj
#         })