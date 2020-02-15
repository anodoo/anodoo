# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.addons.crm.models import crm_stage

class Opportunity(models.Model):    
    _inherit = 'crm.lead'
    
    lead_id = fields.Many2one('crm.lead', string='线索', ondelete='restrict')
    
    opportunity_relation_ids = fields.One2many('anodoo.sfa.opportunity.relation', 'opportunity_id', string='商机与商机关系')
    
    project_id = fields.Many2one('project.project', string='商机项目', ondelete='set null')
    project_name = fields.Char('项目名称', related='project_id.name')
    project_user_id = fields.Many2one('res.users', string='项目负责人', related='project_id.user_id')
    project_task_ids = fields.One2many(related='project_id.task_ids', readonly=True)
    project_task_count = fields.Integer('任务数量', related='project_id.task_count')
    
    @api.model
    def create(self, vals):
        '''
            针对商机,默认创建一个商机团队和项目
        '''
        res = super().create(vals)
        
        #根据配置,是否创建默认商机团队
        if True:
            team_template = self.env['crm.team'].search([('team_type', '=', 'opportunity'), ('is_template', '=', True)], order='sequence', limit=1)
            if team_template:
                for opportunity in res:
                    if opportunity.type == 'opportunity':
                        team_vals = {
                            'name' : opportunity.name,
                            'team_type' : 'opportunity',
                            'description' : '商机' + opportunity.name + "自动根据团队模板创建的商机团队",                            
                            }
                        team = self.env['crm.team'].create(team_vals)
                        opportunity.write({'owner_team_id' : team[0].id})
                    
        
        #根据配置,是否创建默认商机项目
        if True:
            for opportunity in res:
                if opportunity.type == 'opportunity':
                    project_vals = {
                        'name' : opportunity.name,
                        'user_id' : opportunity.user_id.id,
                        'partner_id' : opportunity.partner_id.id,
                        'project_type' : 'opportunity'
                        }
                    project = self.env['project.project'].create(project_vals)
                    opportunity.write({'project_id' : project[0].id})
        

        return res

class OpportunityRelation(models.Model):
    _name = 'anodoo.sfa.opportunity.relation'
    _description = '商机和商机的关系'
    _rec_name = 'opportunity_to_id'
    _order = 'id'
    
    opportunity_id = fields.Many2one('crm.lead', string='商机', domain='[("type", "=", "opportunity")]')
    
    opportunity_to_id = fields.Many2one('crm.lead', string='商机', domain='[("type", "=", "opportunity")]')
    
    relation_type = fields.Selection([('parent', '父商机'), ('child', '子商机'), ('relative', '相关商机')],
        string='关系类型', default='relative', help="商机和商机的关系")
    
    description = fields.Text('说明')
    
class OpportunityRegister(models.Model):
    _name = 'anodoo.sfa.opportunity.register'
    _description = '商机注册,商机报备'
    _rec_name = 'name'
    _order = 'id'
    
    
    name = fields.Char('名称', required=True)
    
    customer_info = fields.Char('客户信息', required=True)
    
    contact_info = fields.Char('联系信息', required=True)
    
    tag_ids = fields.Many2many('crm.lead.tag', 'anodoo_sfa_opportunity_register_tag_rel', 'register_id', 'tag_id', string='商机标签')
    
    priority = fields.Selection(crm_stage.AVAILABLE_PRIORITIES, string='Priority', index=True, default=crm_stage.AVAILABLE_PRIORITIES[0][0])
    
    planned_revenue = fields.Float('预计收入')
    
    date_deadline = fields.Date('预计关闭日期')
    
    description = fields.Text('描述')
    
    def convert_to_opportunity(self):
        pass
    