# -*- coding: utf-8 -*-

from odoo import models, fields, api






class PartnerCategory(models.Model):
    _inherit = 'res.partner.category'

    # 参考res.partner的user_id 如果所属人不为空,则该分类为此人私有
    private_user_id = fields.Many2one('res.users', string='所属人', help="如果所属人不为空,则该分类为此人私有")

