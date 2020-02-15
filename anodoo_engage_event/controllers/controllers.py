# -*- coding: utf-8 -*-
from odoo import http

# class AnodooEngageEvent(http.Controller):
#     @http.route('/anodoo_engage_event/anodoo_engage_event/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_engage_event/anodoo_engage_event/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_engage_event.listing', {
#             'root': '/anodoo_engage_event/anodoo_engage_event',
#             'objects': http.request.env['anodoo_engage_event.anodoo_engage_event'].search([]),
#         })

#     @http.route('/anodoo_engage_event/anodoo_engage_event/objects/<model("anodoo_engage_event.anodoo_engage_event"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_engage_event.object', {
#             'object': obj
#         })