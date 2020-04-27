# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Location(models.Model):
    _inherit = 'anodoo.location'
    
    territory_id = fields.Many2one('anodoo.sale.territory', string='销售区域')

class Customer(models.Model):
    #extend anodoo_base.Partner
    _inherit = 'res.partner'
    
    territory_id = fields.Many2one('anodoo.sale.territory', string='销售区域', help='客户所属销售区域')

class SaleTerritory(models.Model):
    _name = "anodoo.sale.territory"
    _description = '销售区域'
    _parent_store = True
    
    name = fields.Char(string='名称', required=True)
    
    parent_id = fields.Many2one('anodoo.sale.territory', string='父区域', index=True, ondelete='cascade')
    child_ids = fields.One2many('anodoo.sale.territory', 'parent_id', string='子区域')

    parent_path = fields.Char(index=True)
    
    description = fields.Text('描述', translate=False)
    
    type = fields.Selection([('customer', '面向客户'), ('product', '面向产品')], required=True,
        string='类型', default='customer', help="")
    
    is_relate_customer = fields.Boolean('是否关联客户', default=False)
    
    location_ids = fields.One2many("anodoo.location", 'territory_id', string='区域位置')
    
    #display_name = fields.Char(string='Display Name') 
    
    team_ids = fields.Many2many('crm.team', 'sale_territory_team_rel', 'territory_id', 'team_id', string='销售团队', help='负责该销售区域的团队', domain='[("team_type","=","sales")]')
    
    
#     @api.constrains('parent_id')
#     def _check_parent_id(self):
#         if not self._check_recursion():
#             raise ValidationError(_('You can not create recursive tags.'))
# 
#     def name_get(self):
#         """ Return the categories' display name, including their direct
#             parent by default.
# 
#             If ``context['partner_category_display']`` is ``'short'``, the short
#             version of the category name (without the direct parent) is used.
#             The default is the long version.
#         """
#         if self._context.get('partner_category_display') == 'short':
#             return super().name_get()
# 
#         res = []
#         for territory in self:
#             names = []
#             current = territory
#             while current:
#                 names.append(current.name)
#                 current = current.parent_id
#             res.append((territory.id, ' / '.join(reversed(names))))
#         return res
# 
#     @api.model
#     def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
#         args = args or []
#         if name:
#             # Be sure name_search is symetric to name_get
#             name = name.split(' / ')[-1]
#             args = [('name', operator, name)] + args
#         partner_category_ids = self._search(args, limit=limit, access_rights_uid=name_get_uid)
#         return models.lazy_name_get(self.browse(partner_category_ids).with_user(name_get_uid))


    
    