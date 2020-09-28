# -*- coding: utf-8 -*-
from ast import literal_eval

from odoo import models, fields, api

class AuthOAuthProvider(models.Model):
    _inherit = 'auth.oauth.provider'
    
    client_secret = fields.Char(string='Client Secret')
    
    oauth_type = fields.Selection([('odoo', 'Odoo官方'), ('google', 'Google'), ('facebook', 'Facebook'), ('github', 'Github'), ('weixin', '微信'), ('qq', 'QQ'), ('dingding', '钉钉')],
                                   required=True,  string='认证类型', default='odoo', help="选择当前认证所属类型")
    
    other_params = fields.Text('其他参数', help="按照{'key1':'value1','key2':'value2'}格式定义其他参数,格式错误将导致参数不可用")
    
    
    
    def get_other_params(self, key, default=None):
        '''
        获取其他参数
        '''

        
       # if (self.other_params_dict is None):
        try:
            self.other_params_dict = literal_eval(self.other_params)
        except ValueError:
            self.other_params_dict = {}
            return default
            
        return self.other_params_dict.get(key, default)
            
        