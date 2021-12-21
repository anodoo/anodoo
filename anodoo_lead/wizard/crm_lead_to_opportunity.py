# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Lead2OpportunityPartner(models.TransientModel):
 
    _inherit = 'crm.lead2opportunity.partner'
     
    #owner_type = fields.Selection([('team', '分配给线索团队'), ('user', '分配给负责人')], required=True, string='分配方式', default='user', help="线索可以分配给团队负责,或者分配给指定具体人员负责")
     
    #owner_team_id = fields.Many2one('crm.team', string='线索团队')

class Lead2OpportunityMassConvert(models.TransientModel):

    _inherit = 'crm.lead2opportunity.partner.mass'

    #owner_type = fields.Selection([('team', '分配给线索团队'), ('user', '分配给负责人')], required=True, string='分配方式', default='user', help="线索可以分配给团队负责,或者分配给指定具体人员负责")
    
    #owner_team_id = fields.Many2one('crm.team', string='线索团队')
