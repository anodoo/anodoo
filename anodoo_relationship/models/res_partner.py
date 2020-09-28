# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Parnter(models.Model):
    _inherit = 'res.partner'


    contact_relation_contact_ids = fields.One2many('anodoo.contact.relation.contact', 'contact_id', string='相关联系人')

    customer_relation_customer_ids = fields.One2many('anodoo.customer.relation.customer', 'customer_id', string='客户与客户关系')