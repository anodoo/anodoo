# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Customer(models.Model):

    _inherit = 'res.partner'


    is_alloted_bypool = fields.Boolean('通过客户池分配', default=False, help="是否通过多种模式已经分配到人或团队")



