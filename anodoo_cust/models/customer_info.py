from odoo import models, fields, api

class Customer(models.Model):
    #extend anodoo_base.Partner
    _inherit = 'res.partner'
        
    customer_identity = fields.Char('唯一标识信息', help='客户唯一标识信息')
    
    #个人客户
    belong_company = fields.Many2one('res.partner', '工作公司', help='个人客户所工作公司')
    function = fields.Char(string='工作职位')
    

    belong_user_id = fields.Many2one('res.users', string='客户经理', help='客户直接分配的客户经理')
    
    customer_relation_customer_ids = fields.One2many('anodoo.customer.relation.customer', 'customer_id', string='客户与客户关系')
    
    #customer_type = fields.Many2one('anodoo.customer.type', string='客户性质')
    customer_type = fields.Selection([('company', '公司客户'), ('person', '个人客户'), ('family', '家庭客户'), ('government', '政府客户'), ('organization', '组织客户')], 
                           string='客户性质', default='company', help='客户类型定义，可扩展')
    
    
    #customer_size = fields.Many2one('anodoo.customer.size', string='客户规模')
    customer_size = fields.Selection([('KA', '大客户'), ('SMB', '中小客户')], 
                            string='客户规模', default='KA', help='客户规模定义，可扩展')
    
    customer_priority = fields.Selection([('0', 'Low'),  ('1', 'Medium'),  ('2', 'High'), ('3', 'Very High')], string='优先级', index=True, default='0')
    
    lifetime_id = fields.Many2one('anodoo.customer.lifetime', string='客户生命周期', help='客户使用的生命周期定义')
    
    
    
    
    
    lifetime_stage_id = fields.Many2one('anodoo.customer.lifetime.stage', string='客户生命周期阶段', help='客户当前的生命周期阶段', 
                                        domain="[('lifetime_id','=', lifetime_id)]")
    
    customer_label_ids = fields.Many2many('anodoo.customer.label', string='客户标签', help='客户当前的所有标签')
    
    is_alloted = fields.Boolean('是否已分配', default=False, compute='_compute_is_alloted')
    
    #customer_user_ids = ''
    
        
 #   @api.model
  #  def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        
    def _compute_is_alloted(self):    
        for record in self:
            record.is_alloted = False
            
    @api.model
    def default_get(self, default_fields):
        # OVERRIDE
        values = super().default_get(default_fields)
        
        lifetime_id = values.get('lifetime_id')
        if 'lifetime_stage_id' in default_fields and lifetime_id:
            
            lifetime_stage = self.env['anodoo.customer.lifetime.stage'].search([('lifetime_id', '=', lifetime_id)], order="is_default desc, sequence, id")
            values['lifetime_stage_id'] = lifetime_stage[0].id
        
        return  values
'''
切换lifetime_id时，根据当前的lifetime_state_id的类型，切换到新lifetime的对应类型
    @api.onchange('lifetime_id')
    def on_change_lifetime_id(self):
        if not self.lifetime_id:
            return

        current_stage_id = self.lifetime_stage_id
        change_stage_id = None
        
        if not current_stage_id:
            if current_stage_id.is_prospect:
                pass
            elif current_stage_id.is_losing:
                pass
            elif current_stage_id.is_success:
                pass
        
        if not change_stage_id:
            lifetime_stage = self.env['anodoo.customer.lifetime.stage'].search([('lifetime_id', '=', self.lifetime_id)], order="is_default desc, sequence, id")
            self.lifetime_stage_id = lifetime_stage[0]
 '''           
        
'''
潜在客户
'''
class ProspectCustomer(models.Model):
    #extend anodoo_cust.Customer
    _inherit = 'res.partner' 
    
    is_prospect = fields.Boolean('是否潜在客户', compute='_compute_is_prospect', store=True)
        
    @api.depends('lifetime_stage_id')
    def _compute_is_prospect(self):
        for record in self:
            record.is_prospect = False
    
'''流失客户'''
class LosingCustomer(models.Model):
    #extend Customer
    _inherit = 'res.partner' 
    
    is_losing = fields.Boolean('是否流失客户', compute='_compute_is_losing', store=True)
          
    @api.depends('lifetime_stage_id')
    def _compute_is_losing(self):
        for record in self:
            record.is_losing = False
    
'''成功客户'''
class SuccessCustomer(models.Model):
    #extend Customer
    _inherit = 'res.partner'
    
    is_success = fields.Boolean('是否成功客户', compute='_compute_is_success', store=True)
        
    @api.depends('lifetime_stage_id')
    def _compute_is_success(self):
        for record in self:
            record.is_success = False
    
    
class CustomerRelationCustomer(models.Model):
    _name = 'anodoo.customer.relation.customer'
    _description = '客户与客户的关系'
    
    customer_id = fields.Many2one('res.partner', string='客户1', help='客户与客户的关系的主方')
    
    relation_customer_id = fields.Many2one('res.partner', string='客户2', help='客户与客户的关系的从方')
    
    relation_type = fields.Selection([('business', '业务'), ('include', '包含'), ('invest', '投资'), ('dealer', '代理')],
                                     string='关系类型', default='business', required=True, help='客户与客户关系的类型')
    
    is_reverse = fields.Boolean('是否反向关系', default=False, help='客户和客户关系的定义一般都是反向的')
    
    