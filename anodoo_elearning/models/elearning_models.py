# -*- coding: utf-8 -*-

from odoo import _
from odoo import models, fields, api

from odoo.tools.translate import html_translate
 
class SlideChannelCategory(models.Model):
    _name = "slide.channel.category"
    _inherit = ["website.seo.metadata", "website.multi.mixin", 'image.mixin']
    _description = "课程目录"
    _parent_store = True
    _order = "sequence, name"

    name = fields.Char(required=True, translate=True)
    parent_id = fields.Many2one('slide.channel.category', string='父课程目录', index=True)
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('slide.channel.category', 'parent_id', string='子课程目录')
    parents_and_self = fields.Many2many('slide.channel.category', compute='_compute_parents_and_self')
    sequence = fields.Integer(help="序号", index=True)
    website_description = fields.Html('目录说明', sanitize_attributes=False, translate=html_translate)
    
    is_publish = fields.Boolean("是否发布", default=True)

    @api.constrains('parent_id')
    def check_parent_id(self):
        if not self._check_recursion():
            raise ValueError(_('Error ! You cannot create recursive categories.'))

    def name_get(self):
        res = []
        for category in self:
            res.append((category.id, " / ".join(category.parents_and_self.mapped('name'))))
        return res

    def _compute_parents_and_self(self):
        for category in self:
            if category.parent_path:
                category.parents_and_self = self.env['slide.channel.category'].browse([int(p) for p in category.parent_path.split('/')[:-1]])
            else:
                category.parents_and_self = category  
                 