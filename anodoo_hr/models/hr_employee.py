# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrEmployeePrivate(models.Model):

    _inherit = "hr.employee"

    employee_level = fields.Char('人员级别')