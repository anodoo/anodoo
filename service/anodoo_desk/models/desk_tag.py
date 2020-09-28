# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _



class DeskTag(models.Model):
    _name = 'anodoo.desk.tag'
    _description = '标签'
    _order = 'name'

    name = fields.Char('标签名称', required=True)

    color = fields.Integer('Color')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "标签名称已经存在"),
    ]
