# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_anodoo_selfservice_forum = fields.Boolean("自助服务论坛", help='启用自助服务的论坛功能，通过论坛的自助服务板块为客户提供讨论空间')

    module_anodoo_selfservice_elearning = fields.Boolean('自助服务在线学习', help='启用自助服务的在线学习和知识库功能，为客户提供各种学习资源')
