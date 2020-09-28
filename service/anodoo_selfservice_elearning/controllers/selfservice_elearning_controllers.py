# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

from odoo.addons.anodoo_selfservice.controllers.selfservice_controllers import SelfServiceController


class SelfServiceController(SelfServiceController):

    #全局搜索结果
    def _prepare_page_data(self, search=None):
        result = super(SelfServiceController, self)._prepare_page_data(search)

        ConfigParameter = request.env['ir.config_parameter'].sudo()
        elearning_id = ConfigParameter.get_param('anodoo_selfservice.selfservice_elearning_id')


        if elearning_id:
            elearning_id = int(elearning_id)
            elearning = request.env['slide.channel'].browse(elearning_id)
            result['elearning'] = elearning

            domain = []
            if search:
                domain += [('name', 'ilike', search)]

            domain += [('channel_id', '=', elearning_id)]
            questions = request.env['slide.slide'].search(domain)
            result['slides'] = questions[:10]
            result['slides_limit'] = len(questions)
            result['search'] = search

        return result
