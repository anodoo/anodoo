# -*- coding: utf-8 -*-
from odoo import http

# class AnodooTeam(http.Controller):
#     @http.route('/anodoo_team/anodoo_team/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anodoo_team/anodoo_team/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('anodoo_team.listing', {
#             'root': '/anodoo_team/anodoo_team',
#             'objects': http.request.env['anodoo_team.anodoo_team'].search([]),
#         })

#     @http.route('/anodoo_team/anodoo_team/objects/<model("anodoo_team.anodoo_team"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anodoo_team.object', {
#             'object': obj
#         })