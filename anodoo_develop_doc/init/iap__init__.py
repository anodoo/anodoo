# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models
from .models.iap import jsonrpc, charge, authorize, capture, cancel, InsufficientCreditError


'''

有账户模型,  
http://iap.odoo.com  可以理解为odoo提供了一个api平台（类似阿里云api平台），卖家可以在上面发布api，然后任何一个db应用都可以购买。有一些是官方	Odoo IAP提供，有一些第三方提供g
https://iap.odoo.com/iap/all-in-app-services  可以查看所有的卖家服务。
如果使用iap，构建自己的iap，成本太高，涉及服务发布，计费，充值等，可以借助odoo iap，发布自己的iap service。
参考开发指导：https://www.odoo.com/documentation/13.0/webservices/iap.html

连接的是odoo的iap账户
需要构架自己的iap服务端
实体
Iap.account


select * from iap_account;
select * from iap_account_res_company_rel


相关模块
Other		iap	iap	*	应用内购买	工具	TRUE	FALSE	web , base_setup , 
Customer			crm_iap_lead	*	线索生成	CRM	FALSE	FALSE	iap , crm , 
Customer			crm_iap_lead_enrich	*	线索内容自动填充	CRM	FALSE	FALSE	iap , crm , 
Customer			crm_iap_lead_website	*	从网站访问产生潜在客户	CRM	FALSE	FALSE	iap , crm , website_form , crm_iap_lead , 
Customer			partner_autocomplete	*	业务伙伴自动完成	工具	TRUE	FALSE	web , mail , iap , 
Customer			partner_autocomplete_address_extended	*	合作伙伴自动填充扩展了地址自动填充功能	工具	TRUE	FALSE	partner_autocomplete , base_address_extended , 
Other			ocn_client	*	Odoo 云提醒客户端 (OCN)	工具	FALSE	FALSE	iap , mail , web_mobile , 


iap/clearbit/1/lead_mining_request
https://iap.odoo.com/iap/1/credit
/iap/clearbit/1/lead_enrichment_email
/iap/clearbit/1/reveal
/iap/1/authorize
/iap/1/cancel
/iap/1/capture
/iap/1/credit
/iap/services
/iap/1/balance
/iap/partner_autocomplete
/iap/message_send  短信模块
/iap/sms/1/send
/iap/snailmail/1/print
'''
