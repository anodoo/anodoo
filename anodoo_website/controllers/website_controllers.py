# -*- coding: utf-8 -*-

from odoo import http

from odoo.addons.website.controllers.main import Website
from odoo.http import request

class LoginHome(Website):
    
    @http.route()
    def web_login(self, redirect=None, *args, **kw):
       
        response = super(Website, self).web_login(redirect=redirect, *args, **kw)
        if not redirect and request.params['login_success']:
            if request.env['res.users'].browse(request.uid).has_group('base.group_user'):
                redirect = b'/web?' + request.httprequest.query_string
            else:
                redirect = '/' #改/my 为 /
            return http.redirect_with_hash(redirect)
        
        return response