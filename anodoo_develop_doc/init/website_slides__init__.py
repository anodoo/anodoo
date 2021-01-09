# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models
from . import wizard


'''

	依赖
	Website 
	Website_mail
	Website_profile
	Website_rating
	相关模块
	Website_slides_forum
	Website_slides_survey
	网站课程中使用调查
	依赖 website_slides, survey	
	Website_sale_slides
	Mass_mailing_slides
	Hr_skills_slides
	Test_website_slides_full
	未来规划
	课程内容,与统一内容管理系统的关系.
	分享,修改国内的图标
	几个扩展模块的实现方法是，在配置中可以触发几个模块的安装（这几个模块已经引入，但默认不安装。）

slide.channel

slide.channel.tag.group
slide.channel.tag

slide.channel

slide.tag
slide.slide

slide.embed
slide.slide.resource
slide.slide.link

slide.question
"slide.answer


订阅关系
slide.channel.partner
slide.slide.partner
功能说明
 * Integrated course and lesson management
 * Fullscreen navigation
 * Support Youtube videos, Google documents, PDF, images, web pages
 * Test knowledge with quizzes
 * Filter and Tag
 * Statistics

和论坛,问卷调查,邮件营销,电商的联系
    module_website_sale_slides = fields.Boolean(string="Sell on eCommerce")
    module_website_slides_forum = fields.Boolean(string="Forum")
    module_website_slides_survey = fields.Boolean(string="Certifications")
    module_mass_mailing_slides = fields.Boolean(string="Mailing")

Forum
Create a community and let the members help each others
Mailing
Contact all the members of a course via mass mailing
Certifications
Evaluate your students and certify them
Sell on eCommerce
Generate revenues thanks to your courses

课程首页
courses_home

测试数据
salesman,manager,it
课程：
SaaS CC理论学习
手机行业解决方案学习
CX优秀产品研究
Anodoo SFA学习
Odoo 14.0 学习
CRM选型研究
Anodoo CRM学习


'''
