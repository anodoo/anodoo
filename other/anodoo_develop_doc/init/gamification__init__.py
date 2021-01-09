# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models
from . import wizard


'''
基础模块， Website profile依赖这个，gamification_sale_crm，hr_gamification都是用了这个。

类别
HR
功能
配置->积分
论坛中也用这个功能

实体
gamification.challenge 挑战
gamification.challenge.line 挑战和目标的对应关系
gamification.goal.definition
gamification.goal
关系：一个挑战，有多个line，每一个line对应一个目标定义。然后参与的人都会根据line和目标定义，有一个自己的目标值

gamification.karma.rank 等级和对应所需积分的定义

gamification.badge 徽章
gamification.badge.user 徽章送给user的记录
扩展
	Res.users  用户具有积分信息

相关


1.1.1.1.	hr_gamification
	依赖,Gamifiction,hr
	功能
实现在employee上的应用


select * from gamification_karma_rank;

select * from gamification_goal_definition;

1.1.1.2.	Gamification_sale_crm
一个对Gamification模块的测试,放了两个销售的挑战数据而已



'''
