# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models

'''

使用这个模块可以在CRM和销售模块管理销售团队
客户参考大量hr的模块

	相关模块
	Hr_skills
	Hr_skills_survey
	Hr中,人工技能的认证
	依赖:hr_skill, survey
	Hr_recruitment_survey
	面试卷子
	Hr_org_chart
	模型
	Crm.team
	Mail.thread
	扩展
	Res.partner 客户,扩展所属销售团队
	Res.users 客户经理,,扩展所属销售团队
	权限
	新增了一些group和user的关系
	Crm.team
	默认团队
	所属公司
	Leader
	Members
	Favorite members
	收藏再dashboard
	Color
	Views
	Dashboard 


'''
