# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PostSeries(models.Model):
    _name = 'anodoo.blog.post.series'
    _description = '文章所属的系列文章'
    _rec_name = 'name'
    _order = 'sequence'
    
    
    name = fields.Char('名称', required=True)
    
    sequence = fields.Integer('序号', default=10)
        
    description = fields.Text('描述')
    
    website_id = fields.Many2one('website', string='网站', help="文章系列所属的网站,不设置则所有的网站可见")
    
    