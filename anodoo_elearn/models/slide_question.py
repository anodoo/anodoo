# -*- coding: utf-8 -*-

from odoo import models, fields, api

'''
    slide和question的关系改为多对多,则slide_id的required属性改为false
'''
class SlideQuestion(models.Model):
    _inherit = "slide.question"
    
    slide_id = fields.Many2one(required=False)
    
