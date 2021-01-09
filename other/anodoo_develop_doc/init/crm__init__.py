# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models
from . import report
from . import wizard

from odoo import api, SUPERUSER_ID


'''

· 如lead模型，被拆分为两个
	o 使用两个新表
	o 后续考虑同时将数据复制到原表
 
 
CRM模块：用于客户关系管理，将客户价值最大化。
 
l 关键依赖
	n Sales_team,contacts
	n Base_setup,web_tour
	n Mail,resource,digest
 
l 线索和商机是一个对象
	n 设置中是否增加qulify操作
	n 邮件到线索
	n 线索打分
l 线索的创建和相关的数据丰富
	n Vistor到线索
	n Enrich线索,需要购买
	n 自动mining线索
		u 申请,扣除点数(这个太棒)
l Odoo自己的lap功能
l https://iap.odoo.com/
 
l 功能
	n 配置
	n 报表
		u 线索分析,根据不同销售团队的线索量
		u 漏斗分析,根据线索的阶段
		u 活动分析,根据活动类型统计
		u 自动生产的lead分析
	n 线索列表
		u 自动创建
		u OdooBot改为Anodoo机器人
		u 转换为商机,enrich,mark to lost
	n 销售
		u 漏斗,就是商机
		u 团队漏斗
		u 客户(后续放在客户360中)
		u 我的报价单(后续放在报价里)
l 实体
	n 阶段Crm.stage
	n 标签
	n 失去原因
	n Crm.lap.lead.mining.request
	n Crm.reveal.rule vistor到lead的自动转
	n 扩展
		u 销售团队  crm.team
		u 活动类型 mail.activity.type


'''
