from odoo import models, fields, api

   
class CustomerType(models.Model):
    _name = "anodoo.customer.type"
    _description = '客户类型'
    _order = 'sequence'
    
    name = fields.Char('名称', required=True)
    
    sequence = fields.Integer('序号', default=1)
    
    type = fields.Char('类型', required=True, help='客户类型定义，可扩展')
    
    is_default = fields.Boolean('是否默认', default=False)
    
    is_active = fields.Boolean('是否启动', default=True)
    
    description = fields.Text('描述', translate=False)
    
class CustomerSize(models.Model):
    _name = "anodoo.customer.size"
    _description = '客户规模'
    
    name = fields.Char('名称', required=True)
    
    sequence = fields.Integer('序号', default=1)
    
    size = fields.Integer('规模')
    
    is_default = fields.Boolean('是否默认', default=False)
    
    is_active = fields.Boolean('是否启动', default=True)
    
    description = fields.Text('描述', translate=False)

class Customer(models.Model):
    #extend anodoo_base.Partner
    _inherit = 'res.partner'
        
    customer_identity = fields.Char('唯一标识信息', help='客户唯一标识信息')
    
    #使用res_partner.user_id
    #belong_user_id = fields.Many2one('res.users', string='客户经理', help='客户分配的客户经理')
    
    belong_team_id = fields.Many2one('crm.team', string='客户团队', help='客户所属的客户团队')
    
    is_alloted_bypool = fields.Boolean('通过客户池分配', default=False, help="是否通过多种模式已经分配到人或团队")
    
    
    customer_relation_customer_ids = fields.One2many('anodoo.customer.relation.customer', 'customer_id', string='客户与客户关系')
    
    def _default_customer_type(self):
        customer_types = self.env['anodoo.customer.type'].search([], order="is_default desc, sequence", limit=1)
        if customer_types:
                return customer_types[0]
        return self.env['anodoo.customer.type']
    
    
    customer_type = fields.Many2one('anodoo.customer.type', string='客户类型', default=_default_customer_type, domain=[('is_active', '=', True)], help='客户类型定义，可扩展')
    #面向开发者来修改
    #customer_type = fields.Selection([('company', '公司客户'), ('person', '个人客户'), ('family', '家庭客户'), ('government', '政府客户'), ('organization', '组织客户')], 
    #                       string='客户类型', default='company', help='客户类型定义，可扩展')
    customer_type_str = fields.Char(related='customer_type.type')
    
    def _default_customer_size(self):
        customer_sizes = self.env['anodoo.customer.size'].search([], order="is_default desc, sequence", limit=1)
        if customer_sizes:
                return customer_sizes[0]
        return self.env['anodoo.customer.size']
    
    customer_size = fields.Many2one('anodoo.customer.size', string='客户规模', default=_default_customer_size, domain=[('is_active', '=', True)], help='客户规模定义，可扩展')
    #customer_size = fields.Selection([('KA', '大客户'), ('SMB', '中小客户')], 
    #                        string='客户规模', default='KA', help='客户规模定义，可扩展')
    customer_size_int = fields.Integer(related='customer_size.size')
    
    customer_priority = fields.Selection([('0', 'Low'),  ('1', 'Medium'),  ('2', 'High'), ('3', 'Very High')], string='优先级', index=True, default='0')
    
    lifetime_id = fields.Many2one('anodoo.customer.lifetime', string='客户生命周期', help='客户使用的生命周期定义')
    
    lifetime_stage_id = fields.Many2one('anodoo.customer.lifetime.stage', string='客户生命周期阶段', help='客户当前的生命周期阶段', 
                                        domain="[('lifetime_id','=', lifetime_id)]")
    
    is_prospect = fields.Boolean('是否潜在客户', compute='_compute_is_prospect', store=True)
    is_losing = fields.Boolean('是否流失客户', compute='_compute_is_losing', store=True)
    is_success = fields.Boolean('是否成功客户', compute='_compute_is_success', store=True)
    
    

    customer_label_ids = fields.Many2many('anodoo.customer.label', 'anodoo_customer_label_ref', 'customer_id', 'label_id', string='客户标签', help='客户当前的所有标签')
    customer_label_auto_ids = fields.Many2many('anodoo.customer.label', 'anodoo_customer_label_auto_ref', 'customer_id', 'label_id',  string='客户标签(自动)', help='客户自动标签')
    

    #家庭客户
    member_type = fields.Selection([('grandpa', '爷爷'), ('grandma', '奶奶'),('father', '爸爸'), ('mother', '妈妈'),('child1', '孩子'), ('child2', '孩子2')],
        string='成员类型', default='father', help="")
    family_members = fields.One2many('res.partner', 'parent_id', string='家庭成员',  domain=[('partner_type', '=', 'contact')], help="一个家庭客户有多个成员")
    is_contact_members = fields.Boolean('家庭主联系人')
    
    #大客户以上
    test_than_ka = fields.Char('大客户说明')
        
 #   @api.model
  #  def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):

            
    @api.model
    def default_get(self, default_fields):
        # OVERRIDE
        values = super().default_get(default_fields)
        
        lifetime_id = values.get('lifetime_id')
        if 'lifetime_stage_id' in default_fields and lifetime_id:
            
            lifetime_stage = self.env['anodoo.customer.lifetime.stage'].search([('lifetime_id', '=', lifetime_id)], order="is_default desc, sequence, id")
            values['lifetime_stage_id'] = lifetime_stage[0].id
        
        return  values
# '''
# 切换lifetime_id时，根据当前的lifetime_state_id的类型，切换到新lifetime的对应类型
#     @api.onchange('lifetime_id')
#     def on_change_lifetime_id(self):
#         if not self.lifetime_id:
#             return
# 
#         current_stage_id = self.lifetime_stage_id
#         change_stage_id = None
#         
#         if not current_stage_id:
#             if current_stage_id.is_prospect:
#                 pass
#             elif current_stage_id.is_losing:
#                 pass
#             elif current_stage_id.is_success:
#                 pass
#         
#         if not change_stage_id:
#             lifetime_stage = self.env['anodoo.customer.lifetime.stage'].search([('lifetime_id', '=', self.lifetime_id)], order="is_default desc, sequence, id")
#             self.lifetime_stage_id = lifetime_stage[0]
#  '''           
  
    @api.depends('lifetime_id', 'lifetime_stage_id')
    def _compute_is_prospect(self):
        for record in self:
            record.is_prospect = False
    

    
          
    @api.depends('lifetime_id', 'lifetime_stage_id')
    def _compute_is_losing(self):
        for record in self:
            record.is_losing = False
    

    
        
    @api.depends('lifetime_id', 'lifetime_stage_id')
    def _compute_is_success(self):
        for record in self:
            record.is_success = False
            
    @api.onchange('lifetime_id')
    def _onchange_lifetime_id(self):
        LifetimeStage = self.env['anodoo.customer.lifetime.stage']
        
        new_stage = None
        if self.lifetime_stage_id.is_prospect:
            lifetime_stage = LifetimeStage.search([('lifetime_id', '=', self.lifetime_id.id), ('is_prospect', '=', True)], limit=1)
            if lifetime_stage:
                new_stage = lifetime_stage[0]
        elif self.lifetime_stage_id.is_losing:
            lifetime_stage = LifetimeStage.search([('lifetime_id', '=', self.lifetime_id.id), ('is_losing', '=', True)], limit=1)
            if lifetime_stage:
                new_stage = lifetime_stage[0]
        elif self.lifetime_stage_id.is_success:
            lifetime_stage = LifetimeStage.search([('lifetime_id', '=', self.lifetime_id.id), ('is_success', '=', True)], limit=1)
            if lifetime_stage:
                new_stage = lifetime_stage[0]
        if new_stage:
            self.lifetime_stage_id = new_stage
        else:
            lifetime_stage = LifetimeStage.search([('lifetime_id', '=', self.lifetime_id.id)], order="is_default desc, sequence, id", limit=1)
            if lifetime_stage:
                self.lifetime_stage_id = lifetime_stage[0]
            else:
                self.lifetime_stage_id = LifetimeStage
    
    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        context = self._context or {}
        customer_search_mode = context.get('customer_search_mode')
        if customer_search_mode == 'customer_my':
            args += [('user_id', '=', self.env.user.id)]
        elif customer_search_mode == 'customer_myteam':
            args += [('belong_team_id.team_member_ids.user_id', 'in', [self.env.user.id])]

        

        return super()._search(args, offset, limit, order, count=count, access_rights_uid=access_rights_uid)
        
    
    
class CustomerRelationCustomer(models.Model):
    _name = 'anodoo.customer.relation.customer'
    _description = '客户与客户的关系'
    
    customer_id = fields.Many2one('res.partner', string='客户', help='客户与客户的关系的主方')
    
    relation_customer_id = fields.Many2one('res.partner', string='关系客户', domain=[('partner_type', '=', 'customer')], help='客户与客户的关系的从方')
    
    relation_type = fields.Selection([('business', '业务'), ('include', '包含'), ('invest', '投资'), ('dealer', '代理')],
                                     string='关系类型', default='business', required=True, help='客户与客户关系的类型')
    
    is_reverse = fields.Boolean('是否双向关系', default=False, help='客户和客户关系的定义一般都是双向的')
    
    description = fields.Text('备注')
    
