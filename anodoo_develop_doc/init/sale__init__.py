# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models
from . import controllers
from . import report
from . import wizard

from functools import partial
import odoo
from odoo import api, SUPERUSER_ID



'''

该模块包含销售管理和电子商务的所有常见功能。

主要就是报价单和订单
首次进入是会让填写公司信息,报价单样式,并测试发送
Odoo里报价单和订单是一个对象 sale.order


依赖
	Sales_team,Payment,portal,utm
	实体
	Sale.order
	Sale.order.template
	Sale.order.line
	扩展实体
	比较多

'''
