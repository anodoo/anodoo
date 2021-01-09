# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.osv import expression

class Blog(models.Model):
    _inherit = 'blog.blog'
    _order = 'sequence'

    # name = fields.Char('栏目名称')
    # subtitle = fields.Char('栏目概述')

    sequence = fields.Integer('序号', default=10)
    
    is_public = fields.Boolean('是否公开', default=True, help="有些栏目不在列表显示,但可以单独链接浏览")

class BlogPost(models.Model):
    _inherit = "blog.post"
    

    
    series_id = fields.Many2one('anodoo.blog.post.series', string='文章系列', help="当前文章所属的文章系列")
    
    relative_post_ids = fields.Many2many('blog.post', 'anodoo_post_post_relative', 'post_id', 'relative_post_id', string='相关文章', help='本文章的其他相关文章') 
    
    is_public = fields.Boolean('是否公开', default=True, help="有些文章不在列表显示,但可以单独链接浏览")
    
    #拥有控制界面
    is_post_blog_mana2many = fields.Boolean('是否属于多栏目', compute='_compute_is_post_blog_mana2many', help="根据配置计算")
    
    multi_blog_ids = fields.Many2many('blog.blog', 'anodoo_post_blog_many2many', 'post_id', 'blog_id', string='其他栏目', help='一个文章属于多个博客栏目,这里为主栏目的其他栏目')
    
    multi_website_ids = fields.Many2many('website', 'anodoo_post_website_many2many', 'post_id', 'website_id', compute="_compute_multi_website_ids", store=True,  string="其他网站", help='根据文章所与多个栏目,如果栏目属于不同网站,则文章属于多个网站')
    
    website_id = fields.Many2one(related=False, compute='_compute_website_id', store=True)
    
    
    @api.depends('blog_id')
    def _compute_website_id(self):
        for blog_post in self:
            #if blog_post.blog_id:
            blog_post.website_id = blog_post.blog_id.website_id
    
    @api.depends('multi_blog_ids')
    def _compute_multi_website_ids(self):
        for blog_post in self:
            if blog_post.multi_blog_ids:
                website_ids = []
                for blog in blog_post.multi_blog_ids:
                    if blog.website_id:
                        if not self.website_id or blog.website_id.id != self.website_id.id:
                            website_ids.append(blog.website_id.id)
                    
                result = self.env['website'].browse(website_ids)  #self.env['website'].search([('id', 'in', website_ids), ()])

                blog_post.multi_website_ids = result
            else:
                result = self.env['website'].browse([])
                blog_post.multi_website_ids = result
                
                
    def _compute_is_post_blog_mana2many(self):
        is_post_blog_mana2many = self.env["ir.config_parameter"].sudo().get_param("anodoo_blog.is_post_blog_mana2many")
        for record in self:
            record.is_post_blog_mana2many = is_post_blog_mana2many
            
    #Override mixins.py 重写,从而在跨网站发表文章时,不用被当前website限制
    def _search_website_published(self, operator, value):
        
        is_post_blog_mana2many = self.env["ir.config_parameter"].sudo().get_param("anodoo_blog.is_post_blog_mana2many")
        
        if is_post_blog_mana2many:
            
            if not isinstance(value, bool) or operator not in ('=', '!='):
                #logger.warning('unsupported search on website_published: %s, %s', operator, value)
                return [()]
    
            if operator in expression.NEGATIVE_TERM_OPERATORS:
                value = not value
    
            #去掉:不用被当前website限制
    #         current_website_id = self._context.get('website_id')
    #         is_published = [('is_published', '=', value)]
    #         if current_website_id:
    #             on_current_website = self.env['website'].website_domain(current_website_id)
    #             return (['!'] if value is False else []) + expression.AND([is_published, on_current_website])
    #         else:  # should be in the backend, return things that are published anywhere
    #             return is_published    
       
            is_published = [('is_published', '=', value)]
            return is_published 
        else:
            return  super()._search_website_published(operator, value)
            
    @api.depends('is_published', 'website_id')
    @api.depends_context('website_id')
    def _compute_website_published(self):
        is_post_blog_mana2many = self.env["ir.config_parameter"].sudo().get_param("anodoo_blog.is_post_blog_mana2many")
        
        if is_post_blog_mana2many:            
            for record in self:                
                record.website_published = record.is_published
        else:
            super()._compute_website_published()
            