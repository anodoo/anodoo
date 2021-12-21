# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OpportunityLifetime(models.Model):
    _name = 'anodoo.opportunity.lifetime'
    _description = "商机生命周期"
    _rec_name = 'name'
    _order = "is_default desc, sequence"

    name = fields.Char('名称', required=True)

    sequence = fields.Integer('序号', default=1, help="生命周期序号")

    opportunity_domain = fields.Char(string="适用条件", help="可以使用该生命周期的商机")

    description = fields.Text('描述', translate=False)

    is_default = fields.Boolean('默认生命周期', default=False)

    team_id = fields.Many2one('crm.team', string='团队', ondelete='set null',  help='为特定的团队设置生命周期')

    stage_ids = fields.One2many('crm.stage', 'opportunity_lifetime_id', string='生命周期阶段')

class Stage(models.Model):
    _inherit = 'crm.stage'

    opportunity_lifetime_id = fields.Many2one('anodoo.opportunity.lifetime', string='生命周期')
    
    stage_probability = fields.Float('阶段成功率')

    is_qualify = fields.Boolean('是否认定阶段', default=False)
    
    
    