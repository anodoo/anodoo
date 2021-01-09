# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models
from . import wizard
from . import report



'''

		1. event活动(会议,研讨会,展览)
l Event_sms
l Mass_mail_event
l Mass_mailing_event_sms
l Mass_mailing_event_track
l Mass_mailing_event_track_sms
l 相关模块
n Mail
n Portal
 
event
website_event
website_event_sale
			1. Event 线上,线下活动
有网页
定义,管理,跟踪活动和销售活动
 
 
l 依赖
n Base_setup
n Mail
n Portal
l 功能
n Event 应用
n 创建活动
u 日程
u 参加人
u 销售活动门票
u 赞助
l 实体
n Event.type
n Event.event
n Event.registration
n  
n Event.mail
n event.mail.registration
n Event.type.mail
			1. Event_sale
l 依赖
n Event
n Sale_management
			1. website_event线上活动
活动,和活动销售
l 依赖
n Website, website_partner, website_mail
n Event
l  
 
相关模块
l Website_event_sale
n 依赖模块
u Website_sale
u Website_event
u Event_sale
l Website_event_question 活动问题
n 依赖
u Website_event
l Website_event_track高级活动
n Y依赖
u Website_event
n 功能
u Event的track功能
 
 
1. Crm
2. 客户360
Website_customer
Partner_autocomplete 自动完成
Base_geolocalize 地理定位
Partner_autocomplete_address_extend
Base_address_city
Base_address_extended
Phone_validation
 
开票中也有客户列表

来自 <https://d.docs.live.net/416db431d5865d1a/Microwei/A.产品/0.Odoo/Odoo.docx> 

		n 

'''
