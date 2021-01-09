# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, SUPERUSER_ID
from . import controllers
from . import models
from . import wizard
from . import report


def uninstall_hook(cr, registry):
    ''' Need to reenable the `product` pricelist multi-company rule that were
        disabled to be 'overridden' for multi-website purpose
    '''
    env = api.Environment(cr, SUPERUSER_ID, {})
    pl_rule = env.ref('product.product_pricelist_comp_rule', raise_if_not_found=False)
    pl_item_rule = env.ref('product.product_pricelist_item_comp_rule', raise_if_not_found=False)
    multi_company_rules = pl_rule or env['ir.rule']
    multi_company_rules += pl_item_rule or env['ir.rule']
    multi_company_rules.write({'active': True})



'''


很多电商网站都是基于CMS开发电商
https://www.360magento.com/blog/top-ecommerce-platforms/

Magento
woocommerce
	https://wordpress.org/
	https://woocommerce.com/
	WordPress的插件， PHP+MySQL
shopify SaaS 模式



Odoo WooCommerce Connector
	所有：4个 free，10个pay
	https://apps.odoo.com/apps/modules/browse?price=&search=woocommerce#
	by Emipro Technologies Pvt. Ltd.：
	https://apps.odoo.com/apps/modules/13.0/woo_commerce_ept/



https://www.odoo.com/page/open-source-ecommerce

create_customer 创建客户表单功能

	依赖
	Website
	Sale
	Website_payment
	Website_mail,website_form,website_rating
	digest
	实体
	Website
	定义了一些属性。然后通过related放到res_cofig_setting配置中
	价格表，货币，销售人员和销售团队，购物车过期时间，购物车回复邮件模板
	Visitor
	对产品的浏览
	Product
	产品报价
	产品对外目录
	产品模板，产品变体
	图片：product.image 新实体
	Order
	订单，订单行的扩展
	Res.partner
	最后订单
	Ir_http
	增加affiliate_id的处理，也即销售人员
	Digest
	增电商的两个参数
	Crm.team
	负责哪些电商网站
	主要的route
	/shop,包括类目，翻页
	/shop/product
	change_pricelist
	pricelist
	cart
	cart/update
	checkout
	address
	confirm_order


products_categories

option_collapse_products_categories



概述
	所有的website_sale模块都通过配置来安装，除了website_sale_comparison（增加了产品属性分类）,website_sale_stock(在基础配置中直接加入相关配置，有了库存模块，则配送模块是自动安装的)，sale_coupon（直接加了促销的菜单），website_sale_coupon则自动安装，
	因此以上这些模块不能卸载，则默认设置true，并且readonly。 

	产品列表 <template id="products"
	产品详情页 <template id="product"
	购物车页  <template id="cart"


	

产品属性
	help="""- Instantly: All possible variants are created as soon as the attribute and its values are added to a product.
        - Dynamically: Each variant is created only when its corresponding attributes and values are added to a sales order.
        - Never: Variants are never created for the attribute.
        Note: the variants creation mode cannot be changed once the attribute is used on at least one product.""",

	替代，附属产品和可选产品的关系
	产品和变体的图片关系

价格表
	
	价格表的code使用方法
	高级价格表的设置和取消。
	
价格表：group_product_pricelist
高级价格表：group_sale_pricelist=true， 价格表中的计算功能

价格表和促销的关系和区别。
二者都可以针对特定的产品类目，产品，变体的价格进行打折等。价格表相当是对销售价格进行直接作用（可以显示原价格和折扣，或者不显示）。而促销则是通过增加一个订单项，对真正的产品订单项的价格进行冲抵。另外，促销功能更加丰富，可以针对特定的客户等等。


找到当前客户的价格表：_get_partner_pricelist_multi
domain：<class 'list'>: [('active', '=', True), '|', ('website_id', '=', 1), '&', ('website_id', '=', False), '|', ('selectable', '=', 
 True), ('code', '!=', False)]
	也即：website_id为当前网站，或者website_id为空时，则selectable选上或者code不为空

        """ Retrieve the applicable pricelist for given partners in a given company.

            It will return the first found pricelist in this order:
            First, the pricelist of the specific property (res_id set), this one
                   is created when saving a pricelist on the partner form view.
            Else, it will return the pricelist of the partner country group
            Else, it will return the generic property (res_id not set), this one
                  is created on the company creation.
            Else, it will return the first available pricelist
促销：

购物车
	
	sale.order的状态	state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),

	恢复邮件：mail_template_sale_cart_recovery
	订单确认邮件：mail_template_sale_confirmation
	PI发票邮件：email_template_edi_sale
	

wishlist
	登录和未登录
	如何清空购物车？

订单
	订单列表增加“状态”一列
	电商中，报价单也即购物车。分为1小时前的（遗弃购物车）和1小时内的

客户门户
我的订单
列表视图：portal_my_orders
详情视图：sale_order_portal_template
去掉门户的powered by ：portal_record_sidebar

报价
sale_product_configurator
	一个wizard，对可配置产品进行配置，同时对有可选产品的进行选择
	对产品支持可选产品。其中，对订单实现可选产品（sale_order_option_ids）是在sale_management模块
		<page string="Optional Products" name="optional_products"
	相关：


支付
	现在是第三方完成收款，确认订单后，先发货，再开票，再结合第三方系统确认收款，即完成订单？
	前端是否无法形成将购物车推进到“已发送”状态

库存：


配送:是基于销售模块的
	不需要库存的情形（非库存产品，库存产品）
	不需要配送的情形
	扩展顺丰，在odoo市场中找顺丰，以及其他开源的物流对接方案
	website_description测试

顺丰集成
	https://apps.odoo.com/apps/modules/12.0/stock_sf_connector/
	mixoo.cn网提供。mixoo.cn博主侧重在物流模块。

开票
	如果不开票，则电商的功能如何？

销售团队
	
digest模块

会员中心： 搜索：inherit_id="portal.portal_my_home"
报价，订单在sales模块，发票在account模块，project，task在project模块。
lead和opportunity在website_crm_partner_assign模块

website_sale_management 增加了网站，电商里的dashboard

搜索：.o_dashboard_common
website_sale  controllers/backend.py  fetch_dashboard_data()

改进
	数字产品,不用地址
	怎么做纯电商网站(基于odoo的前端.如果是完全作一个前端通过json接口,那就是另一个问题了.
	演示数据
	b2b  b2c的区别
		b2b不含税；用户注册或邀请制
	

//player.youku.com/embed/XMzA1NTEyNjcwMA==
//player.youku.com/embed/XMzA1NTEyOTg3Ng==
//player.youku.com/embed/XMzA1NTEyNjcyMA==
//player.youku.com/embed/XMzA1NTEyNjcxMg==


website_sale_comparison
	product.attribute.category  关联attribute_ids
	扩展:
	product.attribute  关联category_id
	product.template.attribute.line
	product.product  按产品对比

theme
https://apps.odoo.com/apps/themes/browse?order=Relevance

客户要求设计官网，电商网站
odoo第三方的theme如何购买，安装，试用
开发一个主题：就是开发所有的前段template，js，css，基本上不能复用现有的东西了。
一般的做法是后期，找专门做前段的团队。

表单

Sales Order（这个在电商中没有看到）
Create a Customer


'''
