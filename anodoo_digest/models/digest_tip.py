# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models
from odoo.tools.translate import html_translate


class DigestTip(models.Model):
    _inherit = 'digest.tip'

    name = fields.Char('名称')
