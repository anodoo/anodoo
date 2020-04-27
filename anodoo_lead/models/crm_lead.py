# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import crm_stage

class Lead(models.Model):    
    _inherit = 'crm.lead'
    
    name = fields.Char('名称')
    partner_id = fields.Many2one('res.partner', string='客户', domain="['&', ('partner_type', '=', 'customer'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    
    contact_id = fields.Many2one('res.partner', string='联系人', domain="['&', ('partner_type', '=', 'contact'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]", help="关联联系人,自动带出其联系信息")
    
    owner_type = fields.Selection([('team', '分配给线索团队'), ('user', '分配给负责人')], required=True, string='分配方式', default='user', help="线索可以分配给团队负责,或者分配给指定具体人员负责")
    
    user_id = fields.Many2one('res.users', string='线索负责人')
    
    owner_team_id = fields.Many2one('crm.team', string='线索团队')
    owner_team_name = fields.Char('团队名称', related='owner_team_id.name')
    owner_team_description = fields.Text('团队描述')
    #, related='owner_team_id.description'
    
    
    is_qualify = fields.Boolean('是否认定阶段', related='stage_id.is_qualify', default=False)
    
    can_convert = fields.Boolean('是否可转化商机', compute="_compute_can_convert", default=True)
    
    qualify_lost_reason = fields.Many2one('anodoo.lead.qualify.lost.reason', string='认定失败原因')
    
    
    
    def _default_lifetime_id(self):       
        return self._lifetime_find()
    
    lifetime_id = fields.Many2one('anodoo.lead.lifetime', string='生命周期', help='线索或商机使用的生命周期定义', default=_default_lifetime_id, domain=lambda self:[('is_for_lead', '=', True if self.type=='lead' else False)])
    
    @api.depends('stage_id')
    def _compute_can_convert(self):
        for lead in self:
            #根据配置计算,可通过配置实现默认都可以,忽略阶段定义
            
            #根据阶段设置计算
            if self.stage_id and self.stage_id.can_convert:
                can_convert = True
            else:
                can_convert = False
                    
            lead.can_convert = can_convert
            
            
    def action_set_qualify_lost(self, **additional_values):
        """ Lost semantic: probability = 0 or active = False """
        result = self.write({'active': False, 'probability': 0, 'automated_probability': 0, **additional_values})
        self._rebuild_pls_frequency_table_threshold()
        return result
    
    def _stage_find(self, team_id=False, domain=None, order='sequence'):
        lifetime = self._lifetime_find()
        if lifetime:
            search_domain = [('lifetime_id', '=', lifetime.id)]
        else:
            search_domain = []
            
        if domain:
            search_domain += list(domain)   

        
        return super()._stage_find(team_id=team_id, domain=search_domain, order=order)
    
    def _lifetime_find(self):
        search_domain = []
        
        if self.type == 'opportunity':
            search_domain.append(('is_for_lead', '=', False))
        else:
            search_domain.append(('is_for_lead', '=', True))
            
        return self.env['anodoo.lead.lifetime'].search(search_domain, limit=1)   
    

    def merge_opportunity(self, user_id=False, team_id=False):
        '''
            合并线索商机后,将被合并的线索/商机关联到新线索/商机上.
        '''
        return self.super().merge_opportunity(user_id=user_id, team_id=team_id)
    
    def qualify_success(self):
        pass
