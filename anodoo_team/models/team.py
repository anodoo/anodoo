

from odoo import api, fields, models, _



class Team(models.AbstractModel):
    _name = "anodoo.team"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Team"
    _order = "sequence"
    _check_company_auto = True

    name = fields.Char('名称', required=True)
    
    sequence = fields.Integer('序号', default=10)

    description = fields.Text('描述')
    
    active = fields.Boolean(default=True)

    company_id = fields.Many2one(
        'res.company', 
        string='公司',
        default=lambda self: self.env.company, 
        index=True
    )
    
    leader_user_id = fields.Many2one('res.users', string='负责人', check_company=True)
    
    member_user_ids = fields.Many2many(
        'res.users',
        string='成员', 
        check_company=True,
        help="团队成员，一个人可以属于多个团队"
    )
    
    color = fields.Integer(string='颜色索引', help="The color of the channel")

    customer_id = fields.Many2one('res.partner', string='客户', help='如何设置，则该团队为该客户服务')

    resource_calendar_id = fields.Many2one('resource.calendar', '工作时间表',
                                           default=lambda self: self.env.company.resource_calendar_id,
                                           domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")

#
#
# class RoleTeam(models.AbstractModel):
#     _inherit = "anodoo.team"
#
#     use_team_roles = fields.Boolean('是否使用团队角色', default=True)
#
#     team_member_ids = fields.One2many('anodoo.team.member', 'team_id', string='团队成员')
#
#     team_member_count = fields.Integer('成员数量', compute='_compute_team_member_count')
#
#     team_role_ids = fields.Many2many('anodoo.team.role', string='团队角色')
#
#     def _compute_team_member_count(self):
#         for record in self:
#             record.team_member_count = 41