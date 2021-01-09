# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Parnter(models.Model):
    _inherit = 'res.partner'

    #odoo通过child_ids，来为当前联系人关联子联系人，地址等。
    #odoo中，多个联系人和多个联系地址都是通过child_ids来实现的。修改为：多对多的联系人，用独立的many_child_ids来实现。原来的child_ids用来保存多个地址（界面中屏蔽添加联系人）
    many_child_ids = fields.Many2many('res.partner', 'res_partner_many_child_ids_rel', 'partner_id', 'many_partner_id', string="联系人", help="通用的对多对关系,用来实现联系人的子联系人,客户下的联系人.")

    support_many_child_ids = fields.Boolean('是否支持多对多联系人', compute='_compute_support_many_child_ids')

    contact_relation_contact_ids = fields.One2many('anodoo.contact.relation.contact', 'contact_id', string='相关联系人')


    #个人客户或个人联系人的信息扩展
    birth_date = fields.Date(string="出生日期")
    gender_type = fields.Selection(
        [('man', '男'),
         ('woman', '女'),
         ('unknown', '未知'),
        ], string='性别', default='unknown')

    
    #重写父类，名称还是使用本身的名称
    def _get_name(self):
        return self.name

    def _compute_support_many_child_ids(self):
        ConfigParameter = self.env['ir.config_parameter'].sudo()
        support = ConfigParameter.get_param('anodoo_contacts.support_many_child_ids', False)

        for contact in self:
            contact.support_many_child_ids = support