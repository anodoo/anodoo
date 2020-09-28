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


class Users(models.Model):
    _inherit = 'res.users'
    
    @api.model
    def auth_oauth(self, provider, params):
        p = self.env['auth.oauth.provider'].search([('id', '=', provider)], limit=1)[0]
        
        if p.oauth_type == 'dingding' or p.oauth_type == 'github':            
            params['access_token'] = params['code']
       
        return super().auth_oauth(provider, params)
    
    def computeSignature(self, accessKey, timestamp):        
        return str(base64.b64encode(hmac.new(accessKey.encode(encoding="utf-8"), timestamp.encode(encoding="utf-8"), sha256).digest()))
            
    @api.model
    def _auth_oauth_validate(self, provider, access_token):
        oauth_provider = self.env['auth.oauth.provider'].search([('id', '=', provider)], limit=1)[0]
        
        if oauth_provider.oauth_type == 'dingding':     
            
            client_id = oauth_provider.client_id
            client_secret=oauth_provider.client_secret
            time_stamp=str(int(round(time.time()*1000)))
                
            params = dict(
                accessKey=client_id,
                timestamp=time_stamp,
                signature=self.computeSignature(client_secret, time_stamp)
            )
            
            url = "%s?%s" % (oauth_provider.data_endpoint, werkzeug.url_encode(params))
    
            tmp_auth_code = {"tmp_auth_code": access_token}
            
            result = requests.post(url, json=tmp_auth_code ).text
            result = json.loads(result)
            
            validation = {}
            
            if result['errcode'] == 0:
                validation['user_id'] = result['user_info']['openid']
                validation['unionid'] = result['user_info']['unionid']
                validation['name'] = result['user_info']['nick']
            else:
                raise Exception(result['errmsg'])
            
            return validation
        elif oauth_provider.oauth_type == 'github':     
            clientid = oauth_provider.client_id
            clientsecret=oauth_provider.client_secret
            
            params = dict(
                client_id=clientid,
                client_secret = clientsecret,
                code = access_token                
                )
            
            response = requests.get(oauth_provider.validation_endpoint, params).text
            
            access_token = ''
            if response is not False:
                r = response.split('&')
                for p in r:
                    if p != '':
                        t = p.split('=')
                        if t[0] == 'access_token':
                            access_token = t[1]
                            break
            
                
            validation = {}
            
            if access_token != '':
                response = requests.get(oauth_provider.data_endpoint, params={'access_token': access_token})
                result = response.json()
                
                if result['login'] != '':
                    validation.update(result)
                    validation['user_id'] = result['login']
                else:
                    raise Exception(result['message'])
                           
            return validation
        else:
            return super(Users, self)._auth_oauth_validate(provider, access_token)
    
    @api.model
    def _generate_signup_values(self, provider, validation, params):
         
        oauth_uid = validation['user_id']
        email = validation.get('email', '')
        if email is None or email == '':
            email = 'provider_{}_user_{}'.format(provider, oauth_uid)
        name = validation.get('name', '')
        if name is None or name == '':
            name = email
        
        login = validation.get('login', '')
        if login is None or login == '':
            login = email
            
        return {
            'name': name,
            'login': login,
            'email': email,
            'oauth_provider_id': provider,
            'oauth_uid': oauth_uid,
            'oauth_access_token': params['access_token'],
            'active': True,
        }
    

    
    @api.model
    def auth_oauth_dingtalk(self,provide_id,userid):
        user_ids=self.search([('oauth_provider_id','=',provide_id),('oauth_uid','=',userid)])

        if not user_ids or len(user_ids)>1:
            return AccessDenied
        return (self.env.cr.dbname, user_ids[0].login, userid)

    @api.model
    def _check_credentials(self, password):
        try:
            return super()._check_credentials(password)
        except AccessDenied:
            res = self.sudo().search([('id', '=', self.env.uid), ('oauth_uid', '=', password)])
            if not res:
                raise