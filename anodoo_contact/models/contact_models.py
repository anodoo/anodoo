# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class anodoo_contact(models.Model):
#     _name = 'anodoo_contact.anodoo_contact'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class ContactRelationContact(models.Model):
    _name = 'anodoo.contact.relation.contact'
    _description = '联系人与联系人的关系'
    
    contact_id = fields.Many2one('res.partner', string='联系人1', help='联系人与联系人的关系的主方')
    
    relation_contact_id = fields.Many2one('res.partner', string='联系人2', help='联系人与联系人的关系的从方')
    
    relation_type = fields.Selection([('family', '家人'), ('friend', '朋友'), ('work', '同事')],
                                     string='关系类型', default='friend', required=True, help='联系人与联系人关系的类型')
    
    is_reverse = fields.Boolean('是否反向关系', default=False, help='联系人和联系人关系的定义一般都是反向的')