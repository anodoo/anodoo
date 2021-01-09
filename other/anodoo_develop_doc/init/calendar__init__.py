# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models
from . import wizard


'''

划分为客户交互日历,销售日历,营销日历,服务日历,日常日历

有网页

注意: activity和activityType, event, eventType之间的关系

	相关模块
	Website_calendar 预约,日历与客户交互,约会
	Google_calendar
	Calendar_sms(事件发送短信提醒,应该是选择了sms作为提醒方式时,alarmmanager会调用sms)

	依赖
	Base,mail
	功能
	主要是日历功能,日历界面比较炫
	日历中的对象是会议,扩展为mail中的活动的一种特殊类型,有自己的细分类型(标签)
	提醒功能,  默认通知和邮件,sms应该扩展了一种sms
	参与人,邀请和接受邀请
	数据
	提醒的cron配置
	增加alerm配置
	增加demo数据
	增加meeting的活动类型
	增加了邮件提醒的模板
	实体
	Calendar.event  (界面上算meeting)
	Calendar.event.type (界面算会议类型)
	Calendar.attendee 与会者,是否接受
	Calendar.contacts  我的日历显示其他人的日历
	Calendar.alarm 提前通知方式(类型+提前多少分钟)
	Calendar.alarm_manager (虚拟类)
	扩展
	Res.users  获取user的会议
	res.partner  邀请 partner的提醒功能
	
	Mail.activity,  新增会议时,需要调到日历中
	mail.activity.type 增加了会议
	 mail.message 
	

select * from calendar_event;
select * from calendar_event_type;

'''
