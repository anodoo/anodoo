# -*- coding: utf-8 -*-

from odoo import models, fields, api

class QualifyLostReason(models.Model):
    _name = "anodoo.opportunity.qualify.lost.reason"
    _description = '认定失败的理由'

    name = fields.Char('Description', required=True, translate=True)
    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer('序号', default=10, help="序号")