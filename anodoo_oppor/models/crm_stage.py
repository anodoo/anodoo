# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Stage(models.Model):
    _inherit = 'crm.stage'
        
    stage_probability = fields.Float('阶段成功率')
    
    
    
    
    