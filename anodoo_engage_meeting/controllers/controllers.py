# -*- coding: utf-8 -*-
from odoo import http

# class AnodooEngageMeeting(http.Controller):
#     @http.route('/anodoo_engage_meeting/anodoo_engage_meeting/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_engage_meeting/anodoo_engage_meeting/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_engage_meeting.listing', {
#             'root': '/anodoo_engage_meeting/anodoo_engage_meeting',
#             'objects': http.request.env['anodoo_engage_meeting.anodoo_engage_meeting'].search([]),
#         })

#     @http.route('/anodoo_engage_meeting/anodoo_engage_meeting/objects/<model("anodoo_engage_meeting.anodoo_engage_meeting"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_engage_meeting.object', {
#             'object': obj
#         })