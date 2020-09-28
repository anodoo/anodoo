

from odoo import api, fields, models, _



class TeamTemplate(models.Model):
    _name = "anodoo.team.template"
    _description = "团队模板"
    _order = "id desc"

    name = fields.Char('名称', required=True)

    description = fields.Text('描述')

    leader_user_id = fields.Many2one('res.users', string='负责人')

    member_user_ids = fields.Many2many(
        'res.users',
        string='成员',
    )