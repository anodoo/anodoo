# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models

'''


1.1.1.1.1.	Crm_lap_lead
1.1.1.1.2.	Crm_lap_lead_enrich
	依赖
	Iap
	Crm
	功能odoo的iap-service对lead进行内容丰富,收费付费
1.1.1.1.3.	Crm_lap_lead_website
	依赖		
	Iap,
	Crm,website_form
	Crm_iap_lead
	功能
	CRM->配置->lead
	CRM->Report->
	这个需要一个geoip 模块
	每天自动根据reveal.view创建lead
	实体
	Crm.reveal.rule 生成lead的规则
	Crm.reveal.view 生成的lead的记录

select * from crm_reveal_rule;




'''
