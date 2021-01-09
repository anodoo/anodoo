# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from . import models

'''

相关模块：

website_google_map	*	Google 地图	网站	FALSE	FALSE	base_geolocalize , website_partner , 
	website_customer	*	客户参考	网站	FALSE	FALSE	website_crm_partner_assign , website_partner , website_google_map , 
	website_membership	*	在线会员目录	网站	FALSE	FALSE	website_partner , website_google_map , association , website_sale , 
	website_crm_partner_assign	*	经销商	网站	FALSE	FALSE	base_geolocalize , crm , account , website_partner , website_google_map , portal , 

	/google_map/ 调用google map

web_map	*	地图视图	技术设置	TRUE	FALSE	web , base_setup , 
	contacts_enterprise	*	联系人企业版	未归类	TRUE	FALSE	contacts , web_map , 
	crm_enterprise	*	CRM 企业版	CRM	TRUE	FALSE	crm , web_dashboard , web_cohort , web_map , 
	project_enterprise	*	项目企业版	项目	TRUE	FALSE	project , web_map , web_gantt , 
	stock_intrastat	*	库存Intrastat	库存	TRUE	FALSE	stock , web_dashboard , web_cohort , web_map , web_grid , 

https://www.openstreetmap.org/
https://leafletjs.com/

MapBox教程   https://blog.csdn.net/jwdstef/article/details/38760111
	https://www.mapbox.com/
地图汇  http://www.dituhui.com/

'''
