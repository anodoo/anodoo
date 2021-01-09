# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Note(models.Model):

    _inherit = 'note.note'
    
    model = fields.Char(string='Model Name')
    
    res_id = fields.Integer(string='Record ID', help="ID of the target record in the database")
    
    reference = fields.Char(string='Reference', compute='_compute_reference', readonly=True, store=False)
    
    @api.depends('model', 'res_id')
    def _compute_reference(self):
        for res in self:
            res.reference = "%s,%s" % (res.model, res.res_id)
    