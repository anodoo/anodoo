# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date

from odoo.addons.http_routing.models.ir_http import slug


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    selfservice_elearning_id = fields.Many2one('slide.channel', string='自助服务的课程',   config_parameter='anodoo_selfservice.selfservice_elearning_id')

    selfservice_elearning_url = fields.Char(string='自助服务的课程URL', readonly=True, related='selfservice_elearning_id.website_url')
