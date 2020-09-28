# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MergeOpportunity(models.TransientModel):


    _inherit = 'crm.merge.opportunity'
    
    #owner_type = fields.Selection([('team', '分配给线索团队'), ('user', '分配给负责人')], required=True, string='分配方式', default='user', help="线索可以分配给团队负责,或者分配给指定具体人员负责")
    
    #owner_team_id = fields.Many2one('crm.team', string='线索团队')

    @api.model
    def default_get(self, fields):
        '''
            自动计算多个线索中的分配关系
        '''

        record_ids = self._context.get('active_ids')
        result = super().default_get(fields)

        if record_ids:
            opps = self.env['crm.lead'].browse(record_ids)
            #owner_type_set = set()
            user_id_set = set()
            team_id_set = set()
            for opp in opps:
                #owner_type_set.add(opp.owner_type)
                if opp.user_id:
                    user_id_set.add(opp.user_id.id)
                if opp.team_id:
                    team_id_set.add(opp.team_id.id)
            
            #if len(owner_type_set) == 1:
            #    result['owner_type'] = owner_type_set.pop()
            
            if len(user_id_set) == 1:
                result['user_id'] = user_id_set.pop()
                
            if len(team_id_set) == 1:
                result['team_id'] = team_id_set.pop()
                
        return result