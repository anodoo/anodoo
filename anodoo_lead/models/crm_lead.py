# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Lead(models.Model):    
    _inherit = 'crm.lead'
    
    #name = fields.Char('名称')
    
    #继续使用lead自带的partner_id
    #partner_id = fields.Many2one('res.partner', string='客户', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    
    contact_id = fields.Many2one('res.partner', string='联系人', domain="['&', ('type', '=', 'contact'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]", help="关联联系人,自动带出其联系信息")
    
    #owner_type = fields.Selection([('team', '分配给线索团队'), ('user', '分配给负责人')], required=True, string='分配方式', default='user', help="线索可以分配给团队负责,或者分配给指定具体人员负责")
    
    #user_id = fields.Many2one('res.users', string='线索负责人')
    
    #owner_team_id = fields.Many2one('crm.team', string='线索团队')
    #owner_team_name = fields.Char('团队名称', related='owner_team_id.name')
    #owner_team_description = fields.Text('团队描述')
    #, related='owner_team_id.description'


    

    
    
    
    def _default_lead_lifetime_id(self):

        type = self._context.get('default_type')
        if not type:
            type = self.type

        if type == 'lead':
            return self.env['anodoo.lead.lifetime'].search([], limit=1)

        return None

    lead_lifetime_id = fields.Many2one('anodoo.lead.lifetime', string='生命周期', help='线索的生命周期定义', default=_default_lead_lifetime_id)

    def _default_lead_stage_id(self):
        lead_lifetime_id = self.lead_lifetime_id
        if not lead_lifetime_id:
            lead_lifetime_id = self._default_lead_lifetime_id()

        if lead_lifetime_id:
            domain = [('lead_lifetime_id', '=', lead_lifetime_id.id)]
            return self.env['anodoo.lead.stage'].search(domain, order='sequence', limit=1)
        else:
            return None

    lead_stage_id = fields.Many2one('anodoo.lead.stage', string='线索阶段', default=_default_lead_stage_id)

    is_lead_qualify = fields.Boolean('是否认定阶段', related='lead_stage_id.is_qualify', default=False)

    can_convert = fields.Boolean('是否可转化商机', compute="_compute_can_convert", default=True)

    lead_qualify_lost_reason = fields.Many2one('anodoo.lead.qualify.lost.reason', string='线索认定失败原因')

    @api.depends('lead_stage_id')
    def _compute_can_convert(self):
        for lead in self:
            #根据配置计算,可通过配置实现默认都可以,忽略阶段定义
            
            #根据阶段设置计算
            if self.lead_stage_id and self.lead_stage_id.can_convert:
                can_convert = True
            else:
                can_convert = False
                    
            lead.can_convert = can_convert
            
            
    def action_set_lead_qualify_lost(self, **additional_values):
        """ Lost semantic: probability = 0 or active = False """
        result = self.write({'active': False, 'probability': 0, 'automated_probability': 0, **additional_values})
        self._rebuild_pls_frequency_table_threshold()
        return result


    def merge_opportunity(self, user_id=False, team_id=False):
        '''
            合并线索商机后,将被合并的线索/商机关联到新线索/商机上.
        '''
        return super().merge_opportunity(user_id=user_id, team_id=team_id)
    
    def qualify_lead_success(self):
        pass
