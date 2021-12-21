# -*- coding: utf-8 -*-

from odoo import models, fields, api


class KarmaRank(models.Model):
    _inherit = 'gamification.karma.rank'
     
    category = fields.Selection(selection_add=[('elearning', '在线学习')], ondelete={"elearning" : "cascade"})
