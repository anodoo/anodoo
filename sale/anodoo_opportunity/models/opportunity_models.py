# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.addons.crm.models import crm_stage


class OpportunityRelation(models.Model):
    _name = 'anodoo.opportunity.relation'
    _description = '商机和商机的关系'
    _rec_name = 'opportunity_to_id'
    _order = 'id'
    
    opportunity_id = fields.Many2one('crm.lead', string='商机', domain='[("type", "=", "opportunity")]')
    
    opportunity_to_id = fields.Many2one('crm.lead', string='商机', domain='[("type", "=", "opportunity")]')
    
    relation_type = fields.Selection([('parent', '父商机'), ('child', '子商机'), ('relative', '相关商机')],
        string='关系类型', default='relative', help="商机和商机的关系")
    
    description = fields.Text('说明')
    
class OpportunityRegister(models.Model):
    _name = 'anodoo.opportunity.register'
    _description = '商机注册,商机报备'
    _rec_name = 'name'
    _order = 'id'
    
    
    name = fields.Char('名称', required=True)
    
    customer_info = fields.Char('客户信息', required=True)
    
    contact_info = fields.Char('联系信息', required=True)
    
    tag_ids = fields.Many2many('crm.lead.tag', 'anodoo_opportunity_register_tag_rel', 'register_id', 'tag_id', string='商机标签')
    
    priority = fields.Selection(crm_stage.AVAILABLE_PRIORITIES, string='Priority', index=True, default=crm_stage.AVAILABLE_PRIORITIES[0][0])
    
    planned_revenue = fields.Float('预计收入')
    
    date_deadline = fields.Date('预计关闭日期')
    
    description = fields.Text('描述')
    
    def convert_to_opportunity(self):
        pass
    