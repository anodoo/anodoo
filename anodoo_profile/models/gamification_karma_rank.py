# -*- coding: utf-8 -*-

from odoo import models, fields, api


class KarmaRank(models.Model):
    _inherit = 'gamification.karma.rank'
    _order = 'category, karma_min'
    
    category = fields.Selection([
            ('default', '默认'),
        ], string="分类", required=True, default='default',
           help="级别所属的分类")