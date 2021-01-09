# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models
from . import tests
from . import wizard

'''

继承mail，扩展了mail。其实sms也算是mail的message的一种。
扩展phone_validation
扩展iap，实现短信发送服务

相关模块：比较多，都是继承使用sms的能力。

实体：

sms.template
	模板

sms.sms
	一个sms消息，有发送结果记录

sms.api
	调用odoo iap进行发送
	

'''
