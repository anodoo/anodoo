# -*- coding: utf-8 -*-

from odoo import models, fields, api

'''
    slide和link的关系改为多对多,则slide_id的required属性改为false
'''
class SlideLink(models.Model):
    _inherit = 'slide.slide.link'

    slide_id = fields.Many2one(required=False)


class Slide(models.Model):
    _inherit = 'slide.slide'
    
    link_ids = fields.Many2many('slide.slide.link', 'slide_link_ref', 'slide_id', 'link_id', string="参考链接")
    
    links_count = fields.Integer(string="参考链接数量", compute='_compute_links_count')
    
    
    question_ids = fields.Many2many("slide.question", 'slide_question_ref', "slide_id", 'question_id', string="问题")
    
    @api.depends('link_ids')
    def _compute_links_count(self):
        for slide in self:
            slide.links_count = len(slide.link_ids)
    