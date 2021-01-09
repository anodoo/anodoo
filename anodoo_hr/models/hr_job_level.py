
from odoo import api, fields, models

class JobLevel(models.Model):
    _name = "hr.job.level"
    _description = "岗位级别"
    _order = "sequence, name, id"

    name = fields.Char('岗级名称', required=True)
    sequence = fields.Integer('Sequence', default=1)