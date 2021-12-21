# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # group_can_customer_belong_team = fields.Boolean(string="客户可以按团队分配", default=True,implied_group='anodoo_customer.group_can_customer_belong_team')

    # @api.onchange('group_can_customer_belong_team')
    # def _onchange_group_can_customer_belong_team(self):
    #     """ 客户池功能需要客户团队的支持 """
    #     if not self.group_can_customer_belong_team:
    #         self.group_use_customer_pool = False
    #
    # @api.onchange('group_use_customer_pool')
    # def _onchange_group_use_customer_pool(self):
    #     """ 客户池功能需要客户团队的支持 """
    #     if self.group_use_customer_pool:
    #         self.group_can_customer_belong_team = True

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        
        CustomerPool = self.env["anodoo.customer.pool"]
        if self.module_anodoo_customer_pool:
            ResUsers = self.env["res.users"]
            users = ResUsers.search([("share", "=", False), ('active', '=', True)])
            for user in users:
                if not CustomerPool.search([('belong_user_id', '=', user.id)]):
                    values = {
                            'name': user.name + '私人池',
                            'is_private': True,
                            'manager_user_id': user.id,
                            'description':'系统自动创建的个人私有池',
                            'belong_user_id' :user.id,
                        }
                    CustomerPool.create(values)
        else:
            private_user_pools = CustomerPool.search([('belong_user_id', '!=', False)])
            private_user_pools.unlink()
            
        
        
               
            