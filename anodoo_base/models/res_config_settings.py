# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    #产品设置
    
    def _default_anodoo_product(self):
        return self.env['anodoo.product'].search([], limit=1)

    anodoo_product_id = fields.Many2one('anodoo.product', string="anodoo_product", default=_default_anodoo_product, ondelete='cascade')
    
    product_name = fields.Char('产品名称', related='anodoo_product_id.product_name', readonly=False, help="产品名称,可以将Odoo,Anodoo改为自己的产品名称")
    
    product_website = fields.Char('产品官网', related='anodoo_product_id.product_website', readonly=False, help="产品官网,系统很多地方链接到产品官网")
    
    product_logo = fields.Binary('产品Logo', related='anodoo_product_id.product_logo', readonly=False, help="产品Logo,图片形式,在一些地方可以替换Odoo,Anodoo的图片")
    
    product_icon = fields.Binary('产品Icon', related='anodoo_product_id.product_icon', readonly=False, help="产品图标,图片形式,在一些地方可以替换Odoo,Anodoo的图表")
    
    product_description = fields.Text('产品描述', related='anodoo_product_id.product_description', readonly=False)
    
    #系统设置
    
    active_portal_user_count = fields.Integer('外部用户数量', compute="_compute_active_portal_user_count")
    
    active_group_count = fields.Integer('组数量', compute="_compute_active_group_count")
    
    is_only_anodoo_menu = fields.Boolean('仅仅显示Anodoo根菜单', config_parameter='anodoo_base.is_only_anodoo_menu')
    

    def _compute_active_portal_user_count(self):
        active_portal_user_count = self.env['res.users'].sudo().search_count([('share', '=', True)])
        for record in self:
            record.active_portal_user_count = active_portal_user_count
            

    def _compute_active_group_count(self):
        active_group_count = self.env['res.groups'].sudo().search_count([])
        for record in self:
            record.active_group_count = active_group_count
    
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        
        self.env['ir.ui.menu'].only_display_anodoo_menu(self.is_only_anodoo_menu)

            