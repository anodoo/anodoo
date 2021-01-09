# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models
from .tests import test_resource_model


'''

	资源,如开发人员
	实体
	Resource.resource 资源,如开发人员
	
	resource.calendar	工作时间
	resource.calendar.attendance
	resource.calendar.leaves 个体员工的离开时间
	扩展
	res.company, res.users
	为公司,员工增加多个工作时间,默认工作时间
	Mixin
	resource.mixin


'
'''
