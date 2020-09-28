# -*- coding: utf-8 -*-

from odoo import fields, models, api
from email.policy import default


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"
    
    #模块不能卸载，则默认设置true，并且readonly。
    module_website_sale_comparison = fields.Boolean(default=True)
    
    #模块不能卸载，在基础配置中直接加入相关配置
    module_website_sale_stock = fields.Boolean(default=True)
    
        
            