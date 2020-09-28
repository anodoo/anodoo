# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date

from odoo.addons.http_routing.models.ir_http import slug


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    selfservice_forum_id = fields.Many2one('forum.forum', string='自助服务的论坛板块', config_parameter='anodoo_selfservice.selfservice_forum_id')

    selfservice_forum_url = fields.Char(string='自助服务的论坛板块URL', readonly=True, compute='_compute_selfservice_forum_url')

    def _compute_selfservice_forum_url(self):
        if self.selfservice_forum_id:
            self.selfservice_forum_url = '/forum/%s' % slug(self.selfservice_forum_id)
        else:
            self.selfservice_forum_url = False