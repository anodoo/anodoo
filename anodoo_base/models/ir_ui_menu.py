# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date

class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'
    
    is_root_display = fields.Boolean('根目录显示', default=True)
    
#     update ir_ui_menu t1 set external_id=t2.name
#     from (select name,res_id from ir_model_data where model='ir.ui.menu') t2 
#     where t2.res_id=t1.id
    external_id = fields.Char('外部Id')
    
 #   is_anodoo_root_menu = fields.Boolean('是否是Anodoo根目录', compute="_compute_is_anodoo_root_menu", _default=False)
    
    @api.model
    @api.returns('self')
    def get_user_roots(self):
        #重写父方法,增加is_root_display
        return self.search([('parent_id', '=', False), ('is_root_display', '=', True) ])
   
    def only_display_anodoo_menu(self, only_anodoo):
        
        other_menu = self.env.ref('anodoo_base.odoo_other_menus', raise_if_not_found=False)
        
        if only_anodoo:
            #仅仅显示anodoo菜单,则找到所有根菜单,不是anodoo的则迁移
            root_menus = self.search([('parent_id', '=', False)])
            for root in root_menus:
                #以_menu_root_anodoo后缀
                menuitems = self.env['ir.model.data'].sudo().search([ ('res_id', '=', root.id),  ('model', '=', 'ir.ui.menu')])
                xml_id = menuitems[0].name
                if not (xml_id.endswith('_menu_root_anodoo') or xml_id in ('menu_administration', 'menu_management')):
                    root.write({'parent_id':other_menu.id})
        else:
            #不是,则将被迁移的去掉.
            other_menus = self.search([('parent_id', '=', other_menu.id)])
            for other in other_menus:
                other.write({'parent_id':False})
        
        
        
                                  