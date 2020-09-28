# -*- coding: utf-8 -*-

import base64

from odoo import models, fields, api, tools
from odoo.modules.module import get_resource_path

#这个要去掉，直接利用odoo的，在设置中设置
class AnodooProduct(models.Model):
    _name = 'anodoo.product'
    _description = '产品描述和配置,单例实体'
    _rec_name = 'product_name'
    _order = 'id'
    
    def _get_default_favicon(self):
        image_path = get_resource_path('anodoo_base', 'static/src/img/favicon.ico')
        with tools.file_open(image_path, 'rb') as f:
            return base64.b64encode(f.read())
    
    def _default_logo(self):
        image_path = get_resource_path('anodoo_base', 'static/src/img', 'anodoo-logo.png')
        with tools.file_open(image_path, 'rb') as f:
            return base64.b64encode(f.read())
        
    def _default_icon(self):
        image_path = get_resource_path('anodoo_base', 'static/description', 'icon.png')
        with tools.file_open(image_path, 'rb') as f:
            return base64.b64encode(f.read())
        
        
    product_name = fields.Char('名称名称', default="Anodoo", required=True, help="产品名称,可以将Odoo,Anodoo改为自己的产品名称")
        
    product_website = fields.Char('产品官网', default="http://www.anodoo.com", help="产品官网,系统很多地方链接到产品官网")
    
    product_logo = fields.Binary('产品Logo', default=_default_logo, help="产品Logo,图片形式,在一些地方可以替换Odoo,Anodoo的图片")
    
    product_icon = fields.Binary('产品Icon', default=_default_icon, help="产品图标,图片形式,在一些地方可以替换Odoo,Anodoo的图标")
    
    product_description = fields.Text('产品描述')
    
class UserMenuLink(models.Model):
    _name = 'anodoo.usermenu.link'
    _description = '系统右上角的用户菜单额外扩展的链接'
    _rec_name = 'name'
    _order = 'id'
    
    name = fields.Char('名称', required=True)
    
    sequence = fields.Integer('序号', default=10)
    
    description = fields.Text('描述')
    
    active = fields.Boolean('激活', default=True)
    
    isblank = fields.Boolean('是否新窗口', default=True)
    
    url = fields.Char('链接URL')
    
    groups = fields.Char('角色组')
    
    onclick = fields.Text('onclick方法内容', help="设置了url后onclick方法不会被调用")
    
class DataClean(models.Model):
    _name = 'anodoo.data.clean'
    _description = '数据清理功能,不同的数据清理定义一个'
    _rec_name = 'name'
    _order = 'id'
    
    name = fields.Char('名称', required=True)
    
    table_name = fields.Char('数据库表', help="多个数据库表用,号隔开, 提供了表名后按照顺序删除表内的数据")
    
    class_name = fields.Char('调用类名', default="anodoo_base.model.UserMenuLinkTools", help="清理功能所在类,默认为anodoo_base.model.UserMenuLinkTools")
    
    method_name = fields.Char('调用方法名', help="清理功能所在类的方法,可以继承UserMenuLinkTools定义一个新方法")
    
    method_define = fields.Text('调用方法过程', help="清理功能的方法过程")
    
    description = fields.Text('描述')
    
    active = fields.Boolean('激活', default=True)
    
    def action_data_clean(self, **additional_values):
        raise NotImplementedError("请实现anodoo_base.models.base_models.py的action_data_clean方法")
    
    
#参考res.user 的 'res.users.log' 登陆人和登陆时间使用 create_uid, create_date, 但是会被清空
class LoginRecord(models.Model):
    _name = 'anodoo.login.record'    
    _rec_name = 'user_id'
    _order = 'id desc'
    _description = '用户登陆记录'
       
    user_id = fields.Many2one('res.users', string='登陆用户')
    
    login_time = fields.Datetime('登陆时间', default=lambda self: fields.datetime.now())
    
    login_ip = fields.Char(string="登陆IP")
    