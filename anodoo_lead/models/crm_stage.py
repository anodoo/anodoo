# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LeadLifetime(models.Model):
    _name = 'anodoo.lead.lifetime'
    _description = "线索/商机生命周期"
    _rec_name = 'name'
    _order = "is_default desc, sequence, id"
    
    name = fields.Char('名称', required=True)
    
    sequence = fields.Integer('序号', default=1, help="客户生命周期序号")
    
    is_for_lead = fields.Boolean('线索适用', default=True)
    
    lead_domain = fields.Char(string="适用条件", help="可以使用该生命周期的线索或商机")
    
    description = fields.Text('描述', translate=False)
    
    is_default = fields.Boolean('默认生命周期', default=False)
    
    team_id = fields.Many2one('crm.team', string='团队', ondelete='set null',  help='为特定的团队设置生命周期')
        
    stage_ids = fields.One2many('crm.stage', 'lifetime_id', string='生命周期阶段')
    

class Stage(models.Model):
    _inherit = 'crm.stage'
    
    lifetime_id = fields.Many2one('anodoo.lead.lifetime', string='生命周期')
    is_for_lead = fields.Boolean('线索适用', related='lifetime_id.is_for_lead', default=True, store=True)
    
    is_qualify = fields.Boolean('是否认定阶段', default=False)
    
    can_convert = fields.Boolean('是否可转化商机', default=True)
    
    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        default_type = self.env.context.get('default_type')
        default_is_for_lead = self.env.context.get('default_is_for_lead')
        if default_type:
            if default_type == 'lead':
                args.append(('is_for_lead', '=', True))
            else:
                args.append(('is_for_lead', '=', False))
        elif default_is_for_lead:
            if default_is_for_lead:
                args.append(('is_for_lead', '=', True))
            else:
                args.append(('is_for_lead', '=', False))
        else:
            args.append(('is_for_lead', '=', False))        
        
        return super()._search(args = args, offset=offset, limit=limit, order=order, count=count, access_rights_uid=access_rights_uid)
    
    
    
    
    