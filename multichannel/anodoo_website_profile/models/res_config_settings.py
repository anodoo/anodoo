# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    #这个参数还没有应用在哪里？
    need_karma_to_view_profile = fields.Boolean('需要最低积分去查看他人信息', config_parameter='need_karma_to_view_profile')

    # 这个参数还没有应用在哪里？
    need_email_validate = fields.Boolean('需要邮件确认', config_parameter='need_email_validate')
