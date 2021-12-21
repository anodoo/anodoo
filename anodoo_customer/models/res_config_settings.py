# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    group_use_multi_customer_type = fields.Boolean(string="多客户类型",  default=True, implied_group='anodoo_customer.group_use_multi_customer_type')
    
    group_use_multi_customer_size = fields.Boolean(string="多客户规模", default=True,implied_group='anodoo_customer.group_use_multi_customer_size')
    
    group_use_customer_lifetime = fields.Boolean(string="启动客户生命周期管理", default=True,implied_group='anodoo_customer.group_use_customer_lifetime')

    module_anodoo_customer_family = fields.Boolean("启用家庭客户类型")

    module_anodoo_customer_segment = fields.Boolean("启用客户分群管理")

    module_anodoo_customer_pool = fields.Boolean("启用客户池分配客户")

    module_anodoo_customer_user = fields.Boolean("启用客户应用的用户管理")

    @api.onchange('group_use_multi_customer_type')
    def _onchange_group_use_multi_customer_type(self):
        #不支持多客户类型时，则不支持家庭客户
        if not self.group_use_multi_customer_type:
            self.module_anodoo_customer_family = False

    @api.onchange('module_anodoo_customer_family')
    def _onchange_module_anodoo_customer_family(self):
        #家庭客户需要多客户类型功能的支持
        if self.module_anodoo_customer_family:
            self.group_use_multi_customer_type = True


     

            
        
        
               
            