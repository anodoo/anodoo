# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Project(models.Model):
    _inherit = "project.project"
    
    project_type = fields.Selection([('common', '通用项目'), ('customer', '客户项目'), ('opportunity', '商机项目')], required=True,
        string='项目类型', default='common', help="包括通用项目和专用项目")