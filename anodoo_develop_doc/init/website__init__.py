# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models
from . import wizard

import odoo
from odoo import api, SUPERUSER_ID
from functools import partial


def uninstall_hook(cr, registry):
    def rem_website_id_null(dbname):
        db_registry = odoo.modules.registry.Registry.new(dbname)
        with api.Environment.manage(), db_registry.cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, {})
            env['ir.model.fields'].search([
                ('name', '=', 'website_id'),
                ('model', '=', 'res.config.settings'),
            ]).unlink()
    cr.after('commit', partial(rem_website_id_null, cr.dbname))



'''
	/website/info
	/sitemap.xml
	/robots.txt
	 
	 
	 
	l 依赖
		n Web,web_editor,http_routing
		n Portal
		n Social_media
		n Auth_signup
	l 相关模块
			u Website_crm  
		n Website_sms 网站访客发送消息
			u 依赖:website, sms
			u Allows to send sms to website visitor if the visitor is linked to a partner.
		n Website_crm_sms
			u 依赖:website_sms, crm
			u Allows to send sms to website visitor if the visitor is linked to a lead.
		n Website_google_map
	l  
	l 实体
		n Website 网站
		n  
		n Website.page 网站页面， seo是在view对象里
		n Website.menu 上方菜单
		n website.visitor 访问者
		n website.track 访问url记录
		n  
		n website.route  
		n Website.rewrite 重定向
		n  
		n website.seo.metadata
		n  
		n 扩展
			u Res.partner  partner对象属于不同网站，并多网站发布
			u Res.users 不同网站用户
			u Res_lang 网站语言
			u Ir.ui.view 前端视图增加seo，和网站page的关联。一个view关联多个page
	 
	营销相关模块
	l Membership 会员,会员营销
	 
	 
	网站功能
	website
	website_sms
	website_form
	website_links
	website_mail_channel
	website_mass_mailing
	 
	 
	 
	创建网站的过程  default_website
		_bootstrap_homepage: homepage,创建一个home页面
		copy_menu_hierarchy  main_menu菜单体系复制
	 
	加载页面过程
		加载菜单, 在website.layout 中调用<t t-call="website.submenu"> 来修改上一层的视图
		<t t-call-assets="web.assets_common_lazy" t-css="false" lazy_load="True"/>
	            <t t-call-assets="web.assets_frontend_lazy" t-css="false" lazy_load="True"/>
	<template id="page_404">,在视图中搜索404,因为很多都是通过继承来修改的.
	 
	访问者
		如何判断时同一个人  visitor_uuid cookie  _get_visitor_from_request()  
		何时监控: website.ir_http.py  L141  if view and view.track:
	
	来自 <https://d.docs.live.net/416db431d5865d1a/Microwei/A.产品/0.Odoo/Odoo.docx> 

'''
