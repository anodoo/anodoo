from odoo import models, fields, api
from odoo.tools.safe_eval import safe_eval

class CustomerLifetime(models.Model):
    _name = 'anodoo.customer.lifetime'
    _description = "客户生命周期"
    _rec_name = 'name'
    _order = "sequence, id"
    
    name = fields.Char('名称', required=True)
    
    sequence = fields.Integer('序号', default=1, help="客户生命周期序号")
    
    customers_domain = fields.Char(string="适用客户", help="可以使用该生命周期的客户")
    
    description = fields.Text('描述', translate=False)
    
    is_default = fields.Boolean('默认生命周期', default=False)
        
    stage_ids = fields.One2many('anodoo.customer.lifetime.stage', 'lifetime_id', string='生命周期阶段')
    
    def _is_valid_customer(self, customer):
        if self.customers_domain:
            domain = safe_eval(self.customers_domain) + [('id', '=', customer.id)]
            return bool(self.env['res.partner'].search_count(domain))
        else:
            return True
    
class CustomerLifetimeStage(models.Model):
    _name = 'anodoo.customer.lifetime.stage'
    _description = "客户生命周期阶段"
    _rec_name = 'name'
    _order = "sequence, id"
    
    lifetime_id = fields.Many2one('anodoo.customer.lifetime', string='生命周期')
    
    name = fields.Char('名称', required=True)
    sequence = fields.Integer('序号', default=1, help="客户生命周期阶段的序号")
    is_default = fields.Boolean('默认阶段', default=False)
    
    fold = fields.Boolean('合并', default=False)
    description = fields.Text('描述', translate=False)
    
    is_prospect = fields.Boolean('是否潜在客户', default=False)
    is_losing = fields.Boolean('是否流失客户', default=False)
    is_success = fields.Boolean('是否成功客户', default=False)
    
    
    