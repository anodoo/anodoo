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
    
    contact_id = fields.Many2one('res.partner', string='联系人', help='联系人与联系人的关系的主方')
    
    relation_contact_id = fields.Many2one('res.partner', string='关系联系人', domain=[('partner_type', '=', 'contact')], help='联系人与联系人的关系的从方' )
    
    relation_type = fields.Selection([('family', '家人'), ('friend', '朋友'), ('work', '同事')],
                                     string='关系类型', default='friend', required=True, help='联系人与联系人关系的类型')
    
    is_reverse = fields.Boolean('是否双向保存关系', default=False, help='联系人和联系人关系的定义一般都是双方的,可以选择是否双方都保存')
    
    description = fields.Text('备注')

class Contact(models.Model):
    _inherit = 'res.partner'
     
    
    
    relation_contact_ids = fields.One2many('anodoo.contact.relation.contact', 'contact_id', string='相关联系人')
    
    
class PartnerCategory(models.Model):
    _inherit = 'res.partner.category'
    
    #参考res.partner的user_id 如果所属人不为空,则该分类为此人私有
    private_user_id = fields.Many2one('res.users', string='所属人', help="如果所属人不为空,则该分类为此人私有")
    
    