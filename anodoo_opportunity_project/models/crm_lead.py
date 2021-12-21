# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Opportunity(models.Model):
    _inherit = 'crm.lead'

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

        # 根据配置,是否创建默认商机团队
        #
        # if True:
        #     team_template = self.env['crm.team'].search([('team_type', '=', 'opportunity'), ('is_template', '=', True)],
        #                                                 order='sequence', limit=1)
        #     if team_template:
        #         for opportunity in res:
        #             if opportunity.type == 'opportunity':
        #                 team_vals = {
        #                     'name': opportunity.name + "的商机团队",
        #                     'team_type': 'opportunity',
        #                     'description': '商机' + opportunity.name + "自动根据团队模板创建的商机团队",
        #                 }
        #                 team = self.env['crm.team'].create(team_vals)
        #                 opportunity.write({'team_id': team[0].id})


        # 根据配置,是否创建默认商机项目
        if True:
            for opportunity in res:
                if opportunity.type == 'opportunity':
                    project_vals = {
                        'name': opportunity.name,
                        'user_id': opportunity.user_id.id,
                        'partner_id': opportunity.partner_id.id,
                        'project_type': 'opportunity'
                    }
                    project = self.env['project.project'].create(project_vals)
                    opportunity.write({'project_id': project[0].id})

        return res