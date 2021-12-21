# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    #将default=True,默认使用线索
    group_use_lead = fields.Boolean(string="使用线索", default=True)
    
    
            