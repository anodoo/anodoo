# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AnodooPortal(models.Model):
    _name = 'anodoo.portal'
    _description = '门户定义.系统支持多个门户'
    _rec_name = 'name'
    _order = 'id'

    name = fields.Char('名称', required=True)

    code = fields.Char('标识', required=True)

    description = fields.Text('描述')

    active = fields.Boolean('激活', default=True)

    is_default = fields.Boolean('是否默认', default=False)

    view_id = fields.Many2one('ir.ui.view', string='界面视图', ondelete='restrict', required=True)

    group_id = fields.Many2one('res.groups', string='权限组', ondelete='restrict', required=True)






    