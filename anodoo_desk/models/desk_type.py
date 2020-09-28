# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _



class DeskType(models.Model):

    _name = 'anodoo.desk.type'
    _description = '工单类型'
    _order = 'sequence'

    name = fields.Char('类型名称', required=True)

    description = fields.Text(string='描述')

    sequence = fields.Integer(default=10)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "类型名称已经存在！"),
    ]
