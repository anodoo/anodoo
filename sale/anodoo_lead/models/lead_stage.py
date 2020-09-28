# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LeadLifetime(models.Model):
    _name = 'anodoo.lead.lifetime'
    _description = "线索生命周期"
    _rec_name = 'name'
    _order = "is_default desc, sequence"
    
    name = fields.Char('名称', required=True)
    
    sequence = fields.Integer('序号', default=1, help="客户生命周期序号")

    lead_domain = fields.Char(string="适用条件", help="可以使用该生命周期的线索或商机")
    
    description = fields.Text('描述', translate=False)
    
    is_default = fields.Boolean('默认生命周期', default=False)
    
    team_id = fields.Many2one('crm.team', string='团队', ondelete='set null',  help='为特定的团队设置生命周期')
        
    stage_ids = fields.One2many('anodoo.lead.stage', 'lead_lifetime_id', string='生命周期阶段')
    



AVAILABLE_PRIORITIES = [
    ('0', 'Low'),
    ('1', 'Medium'),
    ('2', 'High'),
    ('3', 'Very High'),
]


class LeadStage(models.Model):

    _name = "anodoo.lead.stage"
    _description = "Lead Stages"
    _rec_name = 'name'
    _order = "sequence"


    name = fields.Char('Stage Name', required=True, translate=True)
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    is_won = fields.Boolean('Is Won Stage?')
    requirements = fields.Text('Requirements', help="Enter here the internal requirements for this stage (ex: Offer sent to customer). It will appear as a tooltip over the stage's name.")
    team_id = fields.Many2one('crm.team', string='Sales Team', ondelete='set null',
        help='Specific team that uses this stage. Other teams will not be able to see or use this stage.')
    fold = fields.Boolean('Folded in Pipeline',
        help='This stage is folded in the kanban view when there are no records in that stage to display.')

    # This field for interface only
    team_count = fields.Integer('team_count', compute='_compute_team_count')

    def _compute_team_count(self):
        for stage in self:
            stage.team_count = self.env['crm.team'].search_count([])

    
    lead_lifetime_id = fields.Many2one('anodoo.lead.lifetime', string='生命周期')

    
    is_qualify = fields.Boolean('是否认定阶段', default=False)
    
    can_convert = fields.Boolean('是否可转化商机', default=True)

    
    
    
    