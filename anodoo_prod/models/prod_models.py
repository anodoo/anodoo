# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import models, fields

class ProductTemplate(models.Model):

    _inherit = ['product.template']
    
    type = fields.Selection(selection_add=[('saas', 'SaaS产品'), ('member', '会员产品'), ('software', '软件产品'), ('digit', '数字产品')])
