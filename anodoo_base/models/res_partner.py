# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Anodoo中对res.partner的基类定义
class Parnter(models.Model):
    _inherit = 'res.partner'
    
    #支持customer, contact, address
    partner_type = fields.Char('扩展类型', default='contact', help='Anodoo按照Odoo设计，用来实现contact,customer, dealer等')
    
    many_partners = fields.Many2many('res.partner', 'res_partner_many_partners_rel', 'partner_id', 'many_partner_id', string="联系人", help="通用的对多对关系,用来实现联系人的子联系人,客户下的联系人.")
    
    many_address = fields.One2many('res.partner', 'parent_id', string='地址',  domain=[('partner_type', '=', 'address')], help="一个联系人的多个地址")
    
    #个人客户或个人联系人的信息扩展
    belong_company = fields.Char('工作公司', help='个人所工作公司')    
    function = fields.Char(string='工作职位')
    birth_date = fields.Date(string="出生日期")
    gender_type = fields.Selection(
        [('man', '男'),
         ('woman', '女'),
         ('unknown', '未知'),
        ], string='性别', default='unknown')
    
    company_type = fields.Selection(store=True)
    
    #重写父类，名称还是使用本身的名称
    def _get_name(self):
        return self.name