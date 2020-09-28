# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    social_qq = fields.Char(related='website_id.social_qq', readonly=False)
    social_weixin = fields.Char(related='website_id.social_weixin', readonly=False)
    social_weibo = fields.Char(related='website_id.social_weibo', readonly=False)
    social_tencent_weibo = fields.Char(related='website_id.social_tencent_weibo', readonly=False)
    social_renren = fields.Char(related='website_id.social_renren', readonly=False)

    
    #Override
    @api.depends('website_id', 'social_twitter', 'social_facebook', 'social_github', 'social_linkedin', 'social_youtube', 'social_instagram', 'social_qq', 'social_weixin', 'social_weibo', 'social_tencent_weibo', 'social_renren')
    def has_social_network(self):
        self.has_social_network = self.social_twitter or self.social_facebook or self.social_github \
            or self.social_linkedin or self.social_youtube or self.social_instagram \
            or self.social_qq or self.social_weixin or self.social_weibo or self.social_tencent_weibo or self.social_renren
    
    #Override
    def inverse_has_social_network(self):
        if not self.has_social_network:
            self.social_twitter = ''
            self.social_facebook = ''
            self.social_github = ''
            self.social_linkedin = ''
            self.social_youtube = ''
            self.social_instagram = ''
            self.social_qq = ''
            self.social_weixin = ''
            self.social_weibo = ''
            self.social_tencent_weibo = ''
            self.social_renren = ''
    
    has_social_network = fields.Boolean("显示社交媒体信息", compute=has_social_network, inverse=inverse_has_social_network)
        
            