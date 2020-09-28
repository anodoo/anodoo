# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MergeRule(models.Model):
    _name = 'anodoo.lead.merge.rule'
    _description = '线索重复规则'
    _rec_name = 'name'
    _order = 'id'
    
    
    name = fields.Char('名称', required=True)
    
    sequence = fields.Integer('序号', default=10, help="序号")
    
    description = fields.Text('描述')

    active = fields.Boolean('激活', default=True)
    
    merge_type = fields.Selection([('only_lead', '仅仅线索'), ('only_opportunity', '仅仅商机'), ('lead_opportunity', '线索和商机')], required=True, string='合并范围', default='only_lead', help="线索可以和商机一起排重,合并等")
    
    
    field_ids = fields.Many2many('ir.model.fields', string='判断重复的字段', domain='[("model", "=", "crm.lead")]', help='一个或多个用来判断线索或商机是否重复的字段')
    
    
class MergeRelation(models.Model):
    _name = 'anodoo.lead.merge.relation'
    _description = '线索重复和合并记录'
    _rec_name = 'merge_to_id'
    _order = 'id'
    
    merge_to_id = fields.Many2one('crm.lead', string='线索/商机1')
    
    merge_from_id = fields.Many2one('crm.lead', string='线索/商机2')
    
    is_ignore = fields.Boolean('是否忽略', default=False, help='对于重复的两个线索,是否忽略')
    
    merge_rule_id = fields.Many2one('anodoo.lead.merge.rule', string='重复规则', help='判断重复的相应规则', ondelete='cascade')
    
    is_merged = fields.Boolean('是否已合并', default=False, help='对于已合并的两个线索, 其中一条已经归档')
    
    is_copy = fields.Boolean('是否复制', default=False, help='对于复制的两个线索,他们将不会被判断为重复')
    
    
    