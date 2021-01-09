from odoo import models, fields, api
from odoo.tools.safe_eval import safe_eval

class CustomerPool(models.Model):
    _name = "anodoo.customer.pool"
    _description = '客户池'
    
    name = fields.Char(string='客户池名称', required=True)
     
    is_private = fields.Boolean('是否私有', default=False, help='私有客户池或公有客户池')
        
    is_default_public = fields.Boolean('是否默认公有客户池', default=False)     
    
    manager_user_id = fields.Many2one('res.users', string='管理员')
     
    description = fields.Text('描述', translate=False)    

    belong_user_id = fields.Many2one('res.users', string='所属个人', help='客户池所属用户')
    
    # belong_team_id = fields.Many2one('crm.team', string='所属团队', help='客户池所属团队')
    
    customers_domain = fields.Char(string="匹配客户", help="根据这些规则,自动匹配符合规则的客户到该客户池")
     
    
    dynamic_customer_ids = fields.Many2many('res.partner', 'anodoo_customer_pool_dynamic_rel', 'pool_id', 'customer_id', string='自动客户列表', help='客户池下的动态客户列表，根据客户匹配规则动态计算并刷新')
    
    static_customer_ids = fields.Many2many('res.partner', 'anodoo_customer_pool_static_rel', 'pool_id', 'customer_id', string='手动客户列表', help='手动将客户添加到本客户池',
                                    domain="[('customer_rank', '>', 0)]")
    
    allot_record_ids = fields.One2many('anodoo.customer.allot', 'from_pool_id', string='分配记录', domain=[('allot_type', '=', 'allot')])
    
    get_record_ids = fields.One2many('anodoo.customer.allot', 'to_pool_id', string='领取记录', domain=[('allot_type', '=', 'get')])
    
#     @api.depends('customers_domain')
#     def _compute_dynamic_customer_ids(self):
        
            
    
    def refresh_pool_customer_list(self):
        ResPartner = self.env['res.partner']
        for record in self:
            
            if not record.is_private:
                domain = [('customer_rank', '>', 0), ('user_id', '=', False)]
                if not record.is_default_public and record.customers_domain:
                    domain += safe_eval(record.customers_domain)
                
                record.dynamic_customer_ids = ResPartner.search(domain)
        
        return True
    
    #根据客户匹配条件自动分配私有客户池客户
    def auto_private_customer_list(self):
        pass


class CustomerAllot(models.Model):
    _name = "anodoo.customer.allot"
    _description = '客户池分配动作记录'
    _rec_name = 'customer_id'
    _order = 'id desc'
    
    from_pool_id = fields.Many2one('anodoo.customer.pool', string='源客户池')
    
    to_pool_id = fields.Many2one('anodoo.customer.pool', string='目标客户池')
      
    allot_type = fields.Selection([('allot', '分配'), ('allot_back', '收回'), ('get', '领取'), ('get_back', '退回')], 
                            string='操作类型', default='allot', help='客户池分配动作，可扩展')
    
    customer_id = fields.Many2one('res.partner', string='客户', domain="[('customer_rank', '>', 0)]")
    
    description = fields.Text('描述', translate=False)
    
    #todo:需要加一个标记已经根据分配记录退回
    
    