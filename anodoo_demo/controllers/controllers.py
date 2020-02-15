# -*- coding: utf-8 -*-
# from odoo import http


# class AnodooDemo(http.Controller):
#     @http.route('/anodoo_demo/anodoo_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_demo/anodoo_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_demo.listing', {
#             'root': '/anodoo_demo/anodoo_demo',
#             'objects': http.request.env['anodoo_demo.anodoo_demo'].search([]),
#         })

#     @http.route('/anodoo_demo/anodoo_demo/objects/<model("anodoo_demo.anodoo_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_demo.object', {
#             'object': obj
#         })
