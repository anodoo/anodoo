
from odoo import api, fields, models

class ProjectStage(models.Model):
    _name = "project.stage"
    _description = "Project Stages"
    _order = "sequence, name, id"

    name = fields.Char('Stage Name', required=True)
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")