# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Updating mako environement in order to be able to use slug
try:
    from odoo.addons.mail.models.mail_template import mako_template_env, mako_safe_template_env
    from odoo.addons.http_routing.models.ir_http import slug

    mako_template_env.globals.update({
        'slug': slug,
    })

    mako_safe_template_env.globals.update({
        'slug': slug,
    })
except ImportError:
    pass

from . import controllers
from . import models
from . import wizard



'''
portal
比website更底层的模块。如果是后台人员，直接进入/web。如果没有后台权限，进入/my， 如果安装了website，则进入/.

不算是一个网站的一个前台网页， /my进入
portal_layout 来实现前段页面。如访问/digest/1/unsubscribe，就知道这个页面了。


l 依赖
	n Web,web_editor,htp_routing,mail,
	auth_signup 需要登录认证
l 功能
	n 网站 /my/home
		u 显示客户的报价单,订单,开票信息等
		u 有购物车
l 实体
	n  
l 问题
	n 权限控制怎么实现
	n 每一个user都有一个门户,如何控制只有customer才有门户, 多个user进入同一个customer的门户
			每一个user进去，除了看普通user的东西，还可以看所属customer的信息。
			将user,customer的门户划分开
	n 不要显示官网的那些菜单
		这个是实施的时候设置即可。
	n 界面的那些view在哪里设置的
		u Account 有invoice的部分
		u Sale有quotation和order的部分
	n 怎么交互的
 
 
关于门户的概念：
	门户更多是一个网站，和这里的portal不是一个概念。portal是底层的一个组件，如果需要做客户门户，员工门户，代理商门户，自助服务门户，其都是基于website来做。可以将这些门户组合在一个website内，也可以通过独立部署，是不同的网站。账号可以独立，也可以共享。
 	所以/my,是公共的一个账号管理，不用设置为其他的。不同门户通过不同的域名来实现的。

多网站
	根据多个网站是否使用同一个账户的设置来决定的。使用不同的账号.不同的门户。使用同一个账号,即使不同网站，还是同一个门户.
 
权限
	如果多个门户组合在一起，注册时,自动设置是哪个门户(默认,网站)，根据权限控制菜单。
	website.menu的权限控制。
	/my里的菜单权限控制

 
菜单栏
	不同门户显示名称,菜单
 
界面
	portal_my_home 在document下有一个o_portal_docs div用来注入
		<t t-call="portal.portal_layout"> 定义了,当有detail信息时,一个左右结构
			<t t-call="portal.frontend_layout">
 
portal_docs_entry

'''
