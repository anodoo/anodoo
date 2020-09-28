# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.osv import expression


class Location(models.Model):
    _description = "位置信息"
    _name = 'anodoo.location'
    
    street = fields.Char(string='地址')
    
    city_id = fields.Many2one("res.country.state.city", string='城市', ondelete='restrict', domain="[('state_id', '=?', state_id)]")
    state_id = fields.Many2one("res.country.state", string='省份', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='国家', ondelete='restrict')

#城市
class CountryStateCity(models.Model):
    _description = "Country state city"
    _name = 'res.country.state.city'
    _order = 'code'

    state_id = fields.Many2one('res.country.state', string='State', required=True, domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', required=True)
    
    name = fields.Char(string='City Name', required=True)
    code = fields.Char(string='City Code', help='City Code', required=True)

    _sql_constraints = [
        ('name_code_uniq', 'unique(country_id, state_id, code)', 'The code of the country,state,city must be unique !')
    ]

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        if self.env.context.get('state_id'):
            args = expression.AND([args, [('state_id', '=', self.env.context.get('state_id'))]])
        if self.env.context.get('country_id'):
            args = expression.AND([args, [('country_id', '=', self.env.context.get('country_id'))]])

        if operator == 'ilike' and not (name or '').strip():
            first_domain = []
            domain = []
        else:
            first_domain = [('code', '=ilike', name)]
            domain = [('name', operator, name)]

        first_state_ids = self._search(expression.AND([first_domain, args]), limit=limit, access_rights_uid=name_get_uid) if first_domain else []
        state_ids = first_state_ids + [state_id for state_id in self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid) if not state_id in first_state_ids]
        return models.lazy_name_get(self.browse(state_ids).with_user(name_get_uid))

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "{} ({}{})".format(record.name, record.country_id.code, record.state_id.code)))
        return result
