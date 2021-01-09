# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Project(models.Model):
    _inherit = "project.project"

    project_code = fields.Char('项目编号')

    project_stage = fields.Many2one('project.stage', string='项目阶段')

    project_type = fields.Many2one('project.type', string='项目类型')
