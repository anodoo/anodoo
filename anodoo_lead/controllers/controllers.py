# -*- coding: utf-8 -*-
from odoo import http

# class AnodooLead(http.Controller):
#     @http.route('/anodoo_lead/anodoo_lead/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_lead/anodoo_lead/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_lead.listing', {
#             'root': '/anodoo_lead/anodoo_lead',
#             'objects': http.request.env['anodoo_lead.anodoo_lead'].search([]),
#         })

#     @http.route('/anodoo_lead/anodoo_lead/objects/<model("anodoo_lead.anodoo_lead"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_lead.object', {
#             'object': obj
#         })