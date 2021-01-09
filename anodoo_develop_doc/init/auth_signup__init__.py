# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models

'''
作为web系统，user和注册登录都是基础功能。


配置:
auth_signup.reset_password 是否可重置密码,
auth_signup.invitation_scope 自由注册和邀请模式
base.template_portal_user_id 新注册用户模板，这个可以配置默认权限
    xml中配置了模板用户，然后将id设置到这个参数下。创建用户的时候根据这个来创建。
    其active属性为false，在创建时会将user设置为true
 
/web/login
/web/signup
/web/reset_password
 
auth_signup  继承了web，portal,website继承了他
	auth_oauth oauth2.0
Auth_ldap 基于base的模块
Auth_password_policy 基于base的模块
	auth_password_policy_signup,同时基于auth_signup，一个粘合模块，没有什么内容

Auth_password_policy
	Minimum number of characters passwords must contain, set to 0 to disable.
	扩展了res.config.setting, res_user，以及密码的位数控制widget。

	 
	 
l 功能
	n 第三方认证
	n 页面中有认证和没认证的内容差异
	n 注册完进入首页,而不是/web/my
	n 两个默认用户的配置
	n 内部登陆页面(外部菜单,另外的地址)
	n 登陆页面定制
	n 用户注册,重置密码
l 实体
	n 扩展
		u Res.partner
		u Res.users
			l 重置密码等
 
登陆,sso等作为一个独立的基础模块,参考auth
	https://www.odoo.com/apps/modules/13.0/login_page/  
	https://www.odoo.com/apps/modules/13.0/login_page_purple/


res.user 的用户类型，是三个res_groups，并不是user有这个属性
base.module_category_user_type 下的groups用来区别用户类型
8	"Portal"	"base"	"group_portal"
9	"Public"	"base"	"group_public"
1	"Internal User"	"base"	"group_user"
'''
