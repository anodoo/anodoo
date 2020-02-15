# -*- coding: utf-8 -*-
from odoo import http

# class AnodooContact(http.Controller):
#     @http.route('/anodoo_contact/anodoo_contact/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_contact/anodoo_contact/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_contact.listing', {
#             'root': '/anodoo_contact/anodoo_contact',
#             'objects': http.request.env['anodoo_contact.anodoo_contact'].search([]),
#         })

#     @http.route('/anodoo_contact/anodoo_contact/objects/<model("anodoo_contact.anodoo_contact"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_contact.object', {
#             'object': obj
#         })