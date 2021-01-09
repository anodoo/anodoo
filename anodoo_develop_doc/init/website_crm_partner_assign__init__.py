# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models
from . import report
from . import wizard


'''
l website_crm_partner_assign  经销商
	n 依赖
		u Website_partner,Portal
		u Crm,account
l 功能
	n 按不同级别,分析营业额
l 实体
l Res.partner.grade  合作伙伴级别
l Res.partner.activation 激活
	n 扩展
Res.partner
'''
