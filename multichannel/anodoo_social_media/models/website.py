# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class Website(models.Model):
    _inherit = "website"
    
    def _default_social_qq(self):
        return self.env.ref('base.main_company').social_qq
    
    def _default_social_weixin(self):
        return self.env.ref('base.main_company').social_weixin
    
    def _default_social_weibo(self):
        return self.env.ref('base.main_company').social_weibo
    
    def _default_social_tencent_weibo(self):
        return self.env.ref('base.main_company').social_tencent_weibo
    
    def _default_social_renren(self):
        return self.env.ref('base.main_company').social_renren

    social_qq = fields.Char('QQ', default=_default_social_qq)
    social_weixin = fields.Char('微信', default=_default_social_weixin)
    social_weibo = fields.Char('微博', default=_default_social_weibo)
    social_tencent_weibo = fields.Char('腾讯微博', default=_default_social_tencent_weibo)
    social_renren = fields.Char('人人网', default=_default_social_renren)
    
