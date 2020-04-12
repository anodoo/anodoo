# -*- coding: utf-8 -*-

from odoo import models, fields, api

class IrTranslation(models.Model):
    _inherit = "ir.translation"
    
    anodoo = fields.Boolean('Anodoo标记', default=False)