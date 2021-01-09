# -*- coding: utf-8 -*-

from odoo import http
from odoo.addons.website_slides.controllers.main import WebsiteSlides
from odoo.http import request

class AnodooElearn(WebsiteSlides):

    #扩展课程类目
    @http.route(['/slides',
                 '/slides/category/<int:category>'], type='http', auth="public", website=True)
    def slides_channel_home(self, category=None, **post):
        
        """ Home page for eLearning platform. Is mainly a container page, does not allow search / filter. """
        domain = request.website.website_domain()
        #增加以下两行
        if category:
            domain.append(('category_id', 'child_of', int(category)))
        
        channels_all = request.env['slide.channel'].search(domain)
        if not request.env.user._is_public():
            channels_my = channels_all.filtered(lambda channel: channel.is_member).sorted('completion', reverse=True)[:3]
        else:
            channels_my = request.env['slide.channel']
        channels_popular = channels_all.sorted('total_votes', reverse=True)[:12]
        channels_newest = channels_all.sorted('create_date', reverse=True)[:3]

        achievements = request.env['gamification.badge.user'].sudo().search([('badge_id.is_published', '=', True)], limit=5)
        if request.env.user._is_public():
            challenges = None
            challenges_done = None
        else:
            challenges = request.env['gamification.challenge'].sudo().search([
                ('challenge_category', '=', 'slides'),
                ('reward_id.is_published', '=', True)
            ], order='id asc', limit=5)
            challenges_done = request.env['gamification.badge.user'].sudo().search([
                ('challenge_id', 'in', challenges.ids),
                ('user_id', '=', request.env.user.id),
                ('badge_id.is_published', '=', True)
            ]).mapped('challenge_id')

        users = request.env['res.users'].sudo().search([
            ('karma', '>', 0),
            ('website_published', '=', True)], limit=5, order='karma desc')

        values = self._prepare_user_values(**post)
        values.update({
            'channels_my': channels_my,
            'channels_popular': channels_popular,
            'channels_newest': channels_newest,
            'achievements': achievements,
            'users': users,
            'top3_users': self._get_top3_users(),
            'challenges': challenges,
            'challenges_done': challenges_done,
        })
                
        #以下为扩展的
        website_domain = request.website.website_domain()
        categs_domain = [('parent_id', '=', False)] + website_domain
        Category = request.env['slide.channel.category']
        categs = Category.search(categs_domain)

        
        if category:
            category = Category.search([('id', '=', int(category))], limit=1)
            if not category:
                category = Category
        else:
            category = Category
        
        values.update({
            'category': category,
            'categories': categs
            })

        return request.render('website_slides.courses_home', values)
    
    
    