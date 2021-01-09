# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import wizard
from . import models


'''
	功能
	开票->报表->产品毛利统计
	对每一个产品实例(不是模板),统计
	采购的开票价格,数量
	销售的开票价格,数量
	计算产品毛利

'''
