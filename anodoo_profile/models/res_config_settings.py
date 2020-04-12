# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    need_email_validate = fields.Boolean('需要邮件确认', config_parameter='anodoo_profile.need_email_validate')
    
    need_karma_to_view_profile = fields.Boolean('需要最低积分去查看他人信息', config_parameter='anodoo_profile.need_karma_to_view_profile')
   
    
    
            