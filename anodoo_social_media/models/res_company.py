# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Company(models.Model):
    _inherit = "res.company"

    social_qq = fields.Char('QQ')
    social_weixin = fields.Char('微信')
    social_weibo = fields.Char('微博')
    social_tencent_weibo = fields.Char('腾讯微博')
    social_renren = fields.Char('人人网')
