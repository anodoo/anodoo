# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class Opportunity(models.Model):
    _inherit = 'crm.lead'

    activity_count = fields.Integer(compute='_compute_activity_count', string="商机活动数量")

    @api.depends()
    def _compute_activity_count(self):
        Activity = self.env['mail.activity']

        for lead in self:
            lead.activity_count = Activity.search_count([
                ('res_id', '=', lead.id), ('res_model_id', '=', self.env['ir.model']._get(self._name).id)
            ])

    def action_view_all_activity(self):
        action = self.env.ref('anodoo_process.process_activity_action').read()[0]
        action['context'] = {
            'search_default_res_name': self.name,
            # 'search_default_res_model_id' : self.env['ir.model']._get(self._name).id
        }
        return action

    @api.model
    def create(self, vals):
        '''
            针对商机,创建销售流程中的所有活动
        '''
        res = super().create(vals)

        # 根据配置,是否默认创建销售流程中的所有活动
        if True:
            for opportunity in res:
                opportunity_lifetime_id = opportunity.opportunity_lifetime_id
                if opportunity_lifetime_id:
                    activity_type_list = self.env['mail.activity.type'].search([('opportunity_lifetime_id', '=', opportunity_lifetime_id.id)],
                                                                               order='sequence')

                    model_id = self.env['ir.model']._get(self._name).id

                    for activity_type in activity_type_list:
                        date_deadline = fields.Date.context_today(self)
                        date_deadline = date_deadline + relativedelta(
                            **{activity_type.delay_unit: activity_type.delay_count})

                        activity_vals = {
                            'res_model_id': model_id,
                            'res_id': opportunity.id,
                            'date_deadline': date_deadline,
                            'user_id': activity_type.default_user_id.id or self.env.uid,
                            'activity_type_id': activity_type.id,
                            'summary': activity_type.summary,
                            'note': activity_type.default_description,
                            'automated': True,
                            'color': activity_type.sequence,  # 临时使用
                        }

                        activity = self.env['mail.activity'].create(activity_vals)

        return res