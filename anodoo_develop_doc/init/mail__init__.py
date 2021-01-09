# -*- coding: utf-8 -*-

from . import models
from . import wizard
from . import controllers

'''

重要问题：
    邮件网关,和discuss中的邮件继承关系
    短信网关，和discuss中的邮件继承关系


	配置菜单
	Email下收件服务器
	实体
	Fetchmail.server
	定时服务
	用来每隔5分钟收一次邮件



官方
https://www.odoo.com/page/discuss
https://www.odoo.com/zh_CN/page/discuss-features
介绍
https://blog.csdn.net/weixin_35737303/article/details/79968241
	功能
	站内邮件
	讨论群组
	个人聊天
	# @ 笑脸
	菜单
	设置->技术->email

	实体
	Mail.message.subtype
	Mail.tracking.value
	Mail.message
	关联body,gateway,recipients,tracking
	Mail.mail
	关联body,advanced,attachments,failure reason

	mail.activity
	Mail.activity.type 活动类型

	mail.moderation 渠道黑白名单
	Mail.blacklist群发邮件黑名单
	收件,发件服务器设置
	Mail.template
	Mail.followers 关注者
	Mail.alias 别名
	Mail.channel 群组 有一个看板
	Mail.channel.partner 群组组员关系
	相关

	Digest 摘要邮件



'''


tracking  问题

- ``mail_notrack``: at create and write, do not perform the value tracking
       creating messages
     - ``tracking_disable``: at create and write, perform no MailThread features
       (auto subscription, tracking, post, ...)

       记录tracking值

if not self._context.get('mail_notrack'):  这里
