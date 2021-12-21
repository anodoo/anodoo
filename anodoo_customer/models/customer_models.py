# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CustomerRelationCustomer(models.Model):
    _name = 'anodoo.customer.relation.customer'
    _description = '客户与客户的关系'
    _rec_name = 'customer_id'

    customer_id = fields.Many2one('res.partner', string='客户', help='客户与客户的关系的主方')

    relation_customer_id = fields.Many2one('res.partner', string='关系客户', domain=[('customer_rank', '>', '0')],
                                           help='客户与客户的关系的从方')

    relation_type = fields.Selection([('business', '业务'), ('include', '包含'), ('invest', '投资'), ('dealer', '代理')],
                                     string='关系类型', default='business', required=True, help='客户与客户关系的类型')

    is_reverse = fields.Boolean('是否双向关系', default=False, help='客户和客户关系的定义一般都是双向的')

    description = fields.Text('备注')