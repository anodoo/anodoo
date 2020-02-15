# -*- coding: utf-8 -*-
from odoo import http

# class AnodooEngageEmail(http.Controller):
#     @http.route('/anodoo_engage_email/anodoo_engage_email/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_engage_email/anodoo_engage_email/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_engage_email.listing', {
#             'root': '/anodoo_engage_email/anodoo_engage_email',
#             'objects': http.request.env['anodoo_engage_email.anodoo_engage_email'].search([]),
#         })

#     @http.route('/anodoo_engage_email/anodoo_engage_email/objects/<model("anodoo_engage_email.anodoo_engage_email"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_engage_email.object', {
#             'object': obj
#         })