# -*- coding: utf-8 -*-
# from odoo import http


from odoo import http
from odoo.http import request

import datetime
import os

class DevelopControllers(http.Controller):

    #卸载模块
    @http.route('/dev/uninstall/<model("ir.module.module"):module>', type='http', auth="user")
    def uninstall(self, module=False, *args, **kw):
        module.button_immediate_uninstall()

        print("卸载模块：%s" % module.name)



        
        