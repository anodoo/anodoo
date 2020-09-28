# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ContactRelationContact(models.Model):
    _name = 'anodoo.contact.relation.contact'
    _description = '联系人与联系人的关系'
    _rec_name = 'contact_id'

    contact_id = fields.Many2one('res.partner', string='联系人', help='联系人与联系人的关系的主方')

    relation_contact_id = fields.Many2one('res.partner', string='关系联系人', help='联系人与联系人的关系的从方')

    relation_type = fields.Selection([('family', '家人'), ('friend', '朋友'), ('work', '同事')],
                                     string='关系类型', default='friend', required=True, help='联系人与联系人关系的类型')

    is_reverse = fields.Boolean('是否双向保存关系', default=False, help='联系人和联系人关系的定义一般都是双方的,可以选择是否双方都保存')

    description = fields.Text('备注')


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