# -*- coding: utf-8 -*-

from odoo import models, fields, api






class PartnerCategory(models.Model):
    _inherit = 'res.partner.category'

    # 参考res.partner的user_id 如果所属人不为空,则该分类为此人私有
    private_user_id = fields.Many2one('res.users', string='所属人', help="如果所属人不为空,则该分类为此人私有")



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