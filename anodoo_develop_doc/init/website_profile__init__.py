# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models
from . import controllers


'''

l 依赖
	n Website_partner, gamification
l 功能
	n 启动网站的用户面板
	n 有一定的积分后可以查看别人的会员信息
	 
	 
	website_profile
	 
	用户社区概念,有分社区概念,如论坛,博客,在线学习.
	 
	gamification
	'depends': ['mail', 'web_kanban_gauge'],
	有多个游戏场景,如社区,销售人员,员工等都不一样
	论坛,学习
	 
	web_kanban_gauge
	'depends': ['web'],
This widget allows to display gauges using d3 library

'''
