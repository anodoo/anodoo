# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models
from . import wizard
from . import report

'''
不知道买会籍那个产品列表怎么来的?需要看源码?

相关模块
    association  不太理解作用，仅仅加了一个菜单
    website_membership  外网展现不同的会员

类别:销售
membership

l 依赖
	n account
l 功能
	n 免费会员,付费会员
	n 会员到期自动续费等
	n /members
l 实体
	n Membership.membership_line 代表了一个会员关系，即res.partner和会员product的关系
	n 扩展
		u Res.partner  会员关系
		u Product.product 会员产品， 也即一个个不同的会员的定义
		u Account.move  付款
		u Account.move.line


'''
