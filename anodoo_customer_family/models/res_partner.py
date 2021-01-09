# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Customer(models.Model):

    _inherit = 'res.partner'

    # 家庭客户

    family_members = fields.One2many('res.partner', 'parent_id', string='家庭成员', help="一个家庭客户有多个成员")

    member_type = fields.Selection(
        [('grandpa', '爷爷'), ('grandma', '奶奶'), ('father', '爸爸'), ('mother', '妈妈'), ('child1', '孩子'), ('child2', '孩子2')],
        string='成员类型', default='father', help="")
    is_contact_members = fields.Boolean('家庭主联系人')


