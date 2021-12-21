# -*- coding: utf-8 -*-

from odoo import http

from odoo.addons.web.controllers.main import Home
from odoo.http import request

class LoginHome(Home):

    #例子，用来为•	登陆页, 不同功能不同登陆页，如/crm/login /prm/login等。
    @http.route('/crm/login', type='http', auth="none")
    def crm_login(self, *args, **kw):
        #
        #         path = request.httprequest.path;
        #         if path == '/crm/login':
        request.params['crm_login'] = True

        response = super(LoginHome, self).web_login(*args, **kw)

        return response