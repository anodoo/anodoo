# -*- coding: utf-8 -*-

from odoo import api, fields, models, _



class DeskStage(models.Model):
    _name = 'anodoo.desk.stage'
    _description = '阶段'
    _order = 'sequence'

    name = fields.Char('阶段名称', required=True)

    description = fields.Text(string='描述')

    sequence = fields.Integer('排序', default=10)

    is_close = fields.Boolean( '关闭阶段', help='用来标示工单的打开和关闭状态')

    fold = fields.Boolean('看板中收缩')

    active = fields.Boolean(default=True)

    legend_blocked = fields.Char( '告警消息', default='阻塞中，需要处理', required=True)

    legend_done = fields.Char( '完成消息', default='已完成，等待进入下一个阶段',  required=True)

    legend_normal = fields.Char( '正常消息', default="正常处理中",  required=True)

    template_id = fields.Many2one(
        comodel_name = 'mail.template',
        string='邮件模板',
        domain="[('model', '=', 'anodoo.desk.ticket')]",
        help="当工单到达此阶段则自动向客户发送邮件"
    )

    # desk模块也要增加
    # def unlink(self):
    def _get_closing_stage(self):
        """
            Return the first closing kanban stage or the last stage of the pipe if none
        """
        closed_stage = self.search([('is_close', '=', True)])
        if not closed_stage:
            closed_stage = self.stage_ids[-1]
        return closed_stage
