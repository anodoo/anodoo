# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, SUPERUSER_ID

from . import models
from . import controllers
from . import wizards


def reset_payment_provider(cr, registry, provider):
    env = api.Environment(cr, SUPERUSER_ID, {})
    acquirers = env['payment.acquirer'].search([('provider', '=', provider)])
    acquirers.write({
        'view_template_id': acquirers._get_default_view_template_id().id,
        'provider': 'manual',
        'state': 'disabled',
    })

'''

支付的基础模块

依赖
account

菜单
Invoicing/Configuration/Payments/Payment Acquirers Invoicing/Configuration/Payments/Payment Icons Invoicing/Configuration/Payments/Payment Transactions Invoicing/Configuration/Payments/Saved Payment Data

	实体
	Payment.acquirer 支付方式
	Payment.token 
	Payment.icon 支付图标
	payment.transaction
	扩展
	Account.payment
	Account.move

相关模块

'''
