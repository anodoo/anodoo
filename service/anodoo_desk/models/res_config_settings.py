# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_anodoo_desk_customer = fields.Boolean("启用工单的客户信息，为工单添加客户相关功能")

    module_anodoo_desk_team = fields.Boolean("启用团队管理，通过团队来处理工单")

    module_anodoo_desk_team_autoassign = fields.Boolean("启用团队内工单的自动分配功能")

    module_anodoo_desk_sla = fields.Boolean("启用工单SLA功能")

    module_anodoo_desk_selfservice = fields.Boolean("启用工单自助服务功能")