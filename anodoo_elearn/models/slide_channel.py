# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Channel(models.Model):
    _inherit = 'slide.channel'
    
    category_id = fields.Many2one('slide.channel.category', string="课程目录")
    
    is_template = fields.Boolean("是否课程模板")



