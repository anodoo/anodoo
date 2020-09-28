# -*- coding: utf-8 -*-

import time
import hmac
import base64
from hashlib import sha256

import werkzeug.urls
import werkzeug.utils

from odoo import models, fields, api
from odoo.http import request
import requests
import json


from odoo.exceptions import except_orm, Warning, RedirectWarning,AccessDenied

class Groups(models.Model):
    _inherit = 'res.groups'
    
# update res_groups t1 set external_id=t2.name
# from (select name,res_id from ir_model_data where model='res_groups') t2 
# where t2.res_id=t1.id
    external_id = fields.Char('外部Id')

class Users(models.Model):
    _inherit = 'res.users'
    

    
    @api.model
    def _update_last_login(self):
        
        super()._update_last_login()
        
        user_id = request.env.user.id
        login_ip = request.httprequest.remote_addr
        
        self.env['anodoo.login.record'].create({'user_id':user_id, 'login_ip':login_ip})
        
