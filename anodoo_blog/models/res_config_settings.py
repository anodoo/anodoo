# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    is_hide_footer = fields.Boolean('隐藏网站Footer', config_parameter='anodoo_blog.is_hide_footer')
    
    is_blog_website_mana2many = fields.Boolean('一个栏目属于多个网站', config_parameter='anodoo_blog.is_blog_website_mana2many')
    
    is_post_blog_mana2many = fields.Boolean('一个文章属于多个栏目', config_parameter='anodoo_blog.is_post_blog_mana2many')
    
    
   
    
    
            