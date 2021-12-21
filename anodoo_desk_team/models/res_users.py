
from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    team_ids = fields.Many2many('anodoo.desk.team', string='客服团队')