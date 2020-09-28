# -*- coding: utf-8 -*-

from odoo import http
from odoo.addons.website_profile.controllers.main import WebsiteProfile
from odoo.http import request, route

class AnodooProfile(WebsiteProfile):

    # 增加('category', '=', 'default') 限制
    # Override
    @http.route()
    def view_ranks_badges(self, **kwargs):
        ranks = []
        if 'badge_category' not in kwargs:
            Rank = request.env['gamification.karma.rank']
            ranks = Rank.sudo().search([('category', '=', 'default')], order='karma_min DESC')

        Badge = request.env['gamification.badge']
        badges = Badge.sudo().search(self._prepare_badges_domain(**kwargs))
        badges = sorted(badges, key=lambda b: b.stat_count_distinct, reverse=True)
        values = self._prepare_user_values(searches={'badges': True})

        values.update({
            'ranks': ranks,
            'badges': badges,
            'user': request.env.user,
        })
        return request.render("website_profile.rank_badge_main", values)

    @http.route('/profile/ranks_list', type='http', auth="public", website=True)
    def view_ranks_list(self, **kwargs):
        Rank = request.env['gamification.karma.rank']
        ranks = Rank.sudo().search([('category', '=', 'default')], order='karma_min DESC')

        values = {
            'ranks': ranks,
        }

        return request.render("anodoo_website.rank_list_main", values)

    @http.route('/profile/badges_list', type='http', auth="public", website=True)
    def view_badges_list(self, **kwargs):
        Badge = request.env['gamification.badge']
        badges = Badge.sudo().search(self._prepare_badges_domain(**kwargs))
        badges = sorted(badges, key=lambda b: b.stat_count_distinct, reverse=True)
        values = self._prepare_user_values(searches={'badges': True})

        values.update({
            'badges': badges,
        })
        return request.render("anodoo_website.badge_list_main", values)