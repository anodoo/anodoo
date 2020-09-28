# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _



class DeskChannel(models.Model):

    _name = 'anodoo.desk.channel'
    _description = '工单来源'
    _order = 'sequence'

    name = fields.Char('来源名称', required=True)

    description = fields.Text(string='描述')

    sequence = fields.Integer(default=10)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "来源名称已经存在！"),
    ]
