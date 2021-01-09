# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models
from . import wizard



'''

创建问卷调查和答案分析
有网站
分类:问卷
https://www.odoo.com/page/survey

	依赖
	Mail
	gamification
相关模块
	Website_slides_survey
	网站课程中使用调查
	依赖 website_slides, survey
	Hr_skills_survey
	Hr中,人工技能的认证
	依赖:hr_skill, survey
	Hr_recruitment_survey
	面试卷子
	实体
	Survey.survey
	Survey.user_input
	Survey.user_input_line
	Survey.question 问题
	Survey.label 可选答案
	扩展
	Challenge和badge实现积分制


'''
