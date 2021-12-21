# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Job(models.Model):

    _inherit = "hr.job"

    job_level = fields.Many2one('hr.job.level', string='岗位级别' )