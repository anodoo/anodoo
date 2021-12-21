
from odoo import api, fields, models

class ProjectType(models.Model):
    _name = "project.type"
    _description = "Project Types"
    _order = "sequence, name, id"

    code = fields.Char('Type Code', required=True)
    name = fields.Char('Type Name', required=True)
    sequence = fields.Integer('Sequence', default=1, help="Used to order types. Lower is better.")