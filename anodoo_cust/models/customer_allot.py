from odoo import models, fields, api

class CustomerPool(models.Model):
    _name = "anodoo.customer.pool"
    _description = '客户池'
    
    name = fields.Char(string='客户池名称', required=True)
     
    is_private = fields.Boolean('是否私有', default=False, help='私有客户池或公有客户池')
        
    manager_user_id = fields.Many2one('res.users', string='管理员')
     
    description = fields.Text('描述', translate=False)
    
    belong_user_ids = fields.Many2many('res.users', string='所属个人', help='客户池所属用户，可以是一个或多个')
    
    belong_team_ids = fields.Many2many('crm.team', string='所属团队', help='客户池所属团队，可以是一个或多个')
    
    segment_ids = fields.Many2many('anodoo.customer.segment', string='客户细分', help='客户池通过管理客户细分来是实现动态的客户列表关联')
    
    dynamic_customer_ids = fields.Many2many('res.partner', 'anodoo_customer_pool_dynamic', 'pool_id', 'customer_id', string='动态客户列表', help='客户池下的动态客户列表，根据关联客户细分动态计算并刷新',
                                    compute='_compute_dynamic_customer_ids')
    
    static_customer_ids = fields.Many2many('res.partner', 'anodoo_customer_pool_static', 'pool_id', 'customer_id', string='静态客户列表', help='客户细分下的静态客户列表',
                                    domain="[('partner_type', '=', 'customer')]")
    
    
    def _compute_dynamic_customer_ids(self):
        for record in self:
            record.dynamic_customer_ids

class DefaultPublicCustomerPool(models.Model):   
    _inherit = "anodoo.customer.pool"
    _description = '默认公有客户池'      
    
    is_default_public = fields.Boolean('是否默认公有客户池', default=False)     
            
class PersonCustomerPool(models.Model):   
    _inherit = "anodoo.customer.pool"
    _description = '个人私有客户池'
    
    belong_person_id = fields.Many2one('res.users', string='私有人', help='私有人不为空时，表示这是个人私有客户池')

class CustomerAllot(models.Model):
    _name = "anodoo.customer.allot"
    _description = '客户池分配动作记录'
    _rec_name = 'customer_id'
    _order = 'id desc'
    
    from_pool_id = fields.Many2one('anodoo.customer.pool', string='源客户池')
    
    to_pool_id = fields.Many2one('anodoo.customer.pool', string='目标客户池')
    
    create_uid = fields.Many2one(string='操作人')
    
    create_date = fields.Datetime(string='操作时间')
    
    allot_type = fields.Selection([('allot', '分配'), ('allot_back', '收回'), ('get', '领取'), ('get_back', '退回')], 
                            string='操作类型', default='allot', help='客户池分配动作，可扩展')
    
    customer_id = fields.Many2one('res.partner', string='客户', domain="[('partner_type', '=', 'customer')]")
    
    description = fields.Text('描述', translate=False)
    
    