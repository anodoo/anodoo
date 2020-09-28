# -*- coding: utf-8 -*-

from odoo import models, fields, api

class QualifyLostReason(models.Model):
    _name = "anodoo.lead.qualify.lost.reason"
    _description = '认定失败的理由'
    
    is_for = fields.Char('适用范围', default='lead')

    name = fields.Char('Description', required=True, translate=True)
    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer('序号', default=10, help="序号")