# -*- coding: utf-8 -*-
from odoo import http

# class AnodooEngageSms(http.Controller):
#     @http.route('/anodoo_engage_sms/anodoo_engage_sms/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_engage_sms/anodoo_engage_sms/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_engage_sms.listing', {
#             'root': '/anodoo_engage_sms/anodoo_engage_sms',
#             'objects': http.request.env['anodoo_engage_sms.anodoo_engage_sms'].search([]),
#         })

#     @http.route('/anodoo_engage_sms/anodoo_engage_sms/objects/<model("anodoo_engage_sms.anodoo_engage_sms"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_engage_sms.object', {
#             'object': obj
#         })