# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models
from . import report

'''

l Project_pad
	n 依赖
		u Project, pad
l Project_forecast
	n 计划,企业版
	n 预测需求和资源
 
其他相关模块
l Project_timesheet_holidays
	n 休假和项目管理 ,属于人力资源模块
l Website_form_project
	n 网站前段创建表单,自动生产项目中的任务
	n 依赖
		u Project,website_form(这个企业版?)
			1. Hr_timesheet
l 相关模块
	n Timesheet_grid  企业版
	n hr_timesheet_attendance 工时和出勤
	n project_timesheet_holidays 休假工时
	n sale_timesheet 销售工时
	n sale_timesheet_purchase 销售工时的采购
			2. 工时
https://www.odoo.com/zh_CN/page/timesheet-mobile-app?utm_source=db&utm_medium=module
 
 
Timesheet_grid
Hr_timesheet
Hr_holidays
Hr_timesheet_attendance
Project_timesheet_holidays
 
Sale_timesheet
Sale_timesheet_purchase

'''
