# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models

'''

摘要邮件。

基础模块，各个模块可以创建kpi。然后可以在后台配置不同的邮件（周期，邮件模板），发送不同的kpi给不同的订阅者。
在General Setting中，可以设置所有new用户的默认摘要邮件。
整体来看，系统中并没有创建多少个kpi。且都是在default中就打开这个api了。且是所有人都可以看到这个。
应该是，针对不同的角色，不同的个人，可以订阅哪些摘要邮件，并发送给他。

摘要邮件中除了可以发送kpi，也可以发送tips，用来给特定的角色的人发送一些tips。

如果要扩展自己的kpi，就可以继承digest。如果新建tips，可以在数据中创建。




	问题
	其他模块怎么注册kpi：通过继承digest类增加kpi_,kpi_*_value)
	怎么定时发送的：通过ir_cron_digest_scheduler_action的每天定时任务来发送。

	依赖
	Mail,portal,resource
	依赖portal，实现在邮件中打开页面，不订阅。

	菜单
	Email下的digest邮件
	没有针对tip的菜单。后续可以添加。

	实体
	Digest.tip
	Digest.digest
	扩展
	Res.users 订阅digest摘要


'''
