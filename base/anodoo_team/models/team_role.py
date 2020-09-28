from odoo import models, fields, api


class TeamRole(models.AbstractModel):
    _name = 'anodoo.team.role'
    _description = '团队角色'
    _order = 'sequence'

    name = fields.Char('名称', required=True)

    sequence = fields.Integer('序号', default=10)

    description = fields.Text('描述', translate=False)

    is_leader = fields.Boolean('是否团队负责人', default=False)

    is_default = fields.Boolean('是否默认角色', default=False)

    group_id = fields.Many2one('res.groups', string='关联权限组')


class TeamMember(models.AbstractModel):
    _name = 'anodoo.team.member'
    _description = '团队成员'
    _rec_name = 'user_id'
    _order = 'sequence'

    role_id = fields.Many2one('anodoo.team.role', string='团队角色')

    user_id = fields.Many2one('res.users', string='团队成员')

    sequence = fields.Integer('序号', default=10)

    description = fields.Text('描述', translate=False)