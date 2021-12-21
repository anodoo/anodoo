# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    full_bank_name = fields.Char('账户银行分行全称', required=True)

    bank_note = fields.Char('备注')
