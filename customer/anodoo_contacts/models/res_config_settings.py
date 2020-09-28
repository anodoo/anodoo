# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    support_many_child_ids = fields.Boolean('支持多对多的联系人', config_parameter='anodoo_contacts.support_many_child_ids')
   
    
    
            