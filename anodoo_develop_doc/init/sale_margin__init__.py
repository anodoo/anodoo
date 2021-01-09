# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models      # noqa
from . import report      # noqa


'''

	功能
	基于销售价和成本价,计算一个销售订单的整体毛利
	就是扩展了视图,增加了毛利字段(暂时没有看到)
	依赖
	Sale_management
	实体
	扩展
	Sale.order
	Sale.order.line


'''
