
from odoo import fields, models

#设置个人的目标
class ResUsers(models.Model):
    _inherit = 'res.users'

    desk_target_closed = fields.Float(string='关闭工单数目标', default=1)

    _sql_constraints = [
        ('target_closed_not_zero', 'CHECK(desk_target_closed > 0)', 'You cannot have negative targets'),
    ]

    def __init__(self, pool, cr):
        """ Override of __init__ to add access rights.
            Access rights are disabled by default, but allowed
            on some specific fields defined in self.SELF_{READ/WRITE}ABLE_FIELDS.
        """
        init_res = super(ResUsers, self).__init__(pool, cr)
        desk_fields = [
            'desk_target_closed',
        ]
        # duplicate list to avoid modifying the original reference
        type(self).SELF_WRITEABLE_FIELDS = list(self.SELF_WRITEABLE_FIELDS)
        type(self).SELF_WRITEABLE_FIELDS.extend(desk_fields)
        # duplicate list to avoid modifying the original reference
        type(self).SELF_READABLE_FIELDS = list(self.SELF_READABLE_FIELDS)
        type(self).SELF_READABLE_FIELDS.extend(desk_fields)
        return init_res
