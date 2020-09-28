# -*- coding: utf-8 -*-

from odoo import models, fields, api

#团队
class Team(models.Model):
    
    _inherit = 'crm.team'
    
    team_type = fields.Selection([('marketing', '营销团队'), ('sales', '销售团队'), ('service', '服务团队'), ('customer', '客户团队'), ('lead', '线索团队'), ('opportunity', '商机团队'), ('project', '项目团队'), ('product', '产品团队'), ('other', '其他团队')], 
                           string='团队类型', default='sales', help='团队类型定义，可扩展')
    
    #不使用odoo原来的lead模式
    team_leader_id = fields.Many2one('anodoo.team.member', string='团度负责人')
    
    #不是用原来的模式
    team_member_ids = fields.One2many('anodoo.team.member', 'team_id', string='团队成员')
    
    team_member_count = fields.Integer('成员数量', compute='_compute_team_member_count')
    
    team_roles = fields.Many2many('anodoo.team.role', 'anodoo_team_role_rel', 'team_id', 'role_id', string='团队角色')
    
    is_template = fields.Boolean('团队模板', default=False)
    
    description = fields.Text('描述')
    
    def _compute_team_member_count(self):
        for record in self:
            record.team_member_count = 41
    

class TeamRole(models.Model):
    _name = 'anodoo.team.role'
    _description = '团队角色'
    _order = 'sequence'
    
    name = fields.Char('名称', required=True)
    
    sequence = fields.Integer('序号', default=10)
    
    description = fields.Text('描述', translate=False)
        
    is_leader = fields.Boolean('是否团队负责人', default=False)
    
    is_default = fields.Boolean('是否默认角色', default=False)
    
    group_id = fields.Many2one('res.groups', string='关联权限组')
    
class TeamMember(models.Model):
    _name = 'anodoo.team.member'
    _description = '团队成员'
    _rec_name = 'user_id'
    _order = 'sequence'
    
    team_id = fields.Many2one('crm.team', string='团队')
    
    role_id = fields.Many2one('anodoo.team.role', string='团队角色')
    
    user_id = fields.Many2one('res.users', string='团队成员')
    
    sequence = fields.Integer('序号', default=10)
    
    description = fields.Text('描述', translate=False)
    
    
    