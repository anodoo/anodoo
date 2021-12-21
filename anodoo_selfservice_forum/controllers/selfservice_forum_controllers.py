# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

from odoo.addons.anodoo_selfservice.controllers.selfservice_controllers import SelfServiceController


class SelfServiceController(SelfServiceController):

    #全局搜索结果
    def _prepare_page_data(self, search=None):
        result = super(SelfServiceController, self)._prepare_page_data(search)

        ConfigParameter = request.env['ir.config_parameter'].sudo()
        forum_id = ConfigParameter.get_param('anodoo_selfservice.selfservice_forum_id')


        if forum_id:
            forum_id = int(forum_id)
            forum = request.env['forum.forum'].browse(forum_id)
            result['forum'] = forum

            domain = []
            if search:
                domain += [('name', 'ilike', search)]

            domain += [('forum_id', '=', forum_id), ('parent_id', '=', False)]
            questions = request.env['forum.post'].search(domain)
            result['questions'] = questions[:10]
            result['questions_limit'] = len(questions)
            result['search'] = search

        return result
