# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request



class SelfServiceController(http.Controller):

    #全局搜索结果
    def _prepare_page_data(self, search=None):
        return {}

    @http.route(['/selfservice/'], type='http', auth="public", website=True)
    def selfservice(self, **kwargs):
        search = kwargs.get('search')

        result = self._prepare_page_data(search=search)

        return request.render("anodoo_selfservice.selfservice", result)
