# -*- coding: utf-8 -*-
from odoo import http

# class AnodooEngageWebsite(http.Controller):
#     @http.route('/anodoo_engage_website/anodoo_engage_website/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_engage_website/anodoo_engage_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_engage_website.listing', {
#             'root': '/anodoo_engage_website/anodoo_engage_website',
#             'objects': http.request.env['anodoo_engage_website.anodoo_engage_website'].search([]),
#         })

#     @http.route('/anodoo_engage_website/anodoo_engage_website/objects/<model("anodoo_engage_website.anodoo_engage_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_engage_website.object', {
#             'object': obj
#         })