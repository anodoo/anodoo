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


    

    
