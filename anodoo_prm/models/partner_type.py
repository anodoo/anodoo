# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PartnerType(models.Model):
    _name = 'anodoo.partner.type'
    _description = '伙伴类型'

    sequence = fields.Integer('排序')

    name = fields.Char('类型名称', translate=True)
