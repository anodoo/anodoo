# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models
from . import report
from . import wizard


'''


待办
	产品的可销售范围：sale_territory_ids，后续放在销售管理中
	成本，不同批次进货价格不同，如何体现在成本里？

demo数据
	两个服务没有发布



待测试：
	
	测试无库存，不配送，不开票的情形
	时区设置

代办：
	产品列表可以增加一个“电商目录”字段
	列表中的可选字段是如何实现的？
	特定用户的价格表好像取得有问题：理论上设置了网站就会显示？购物车有历史价格表时无法选择新的价格表？
	商品清空的购物车是什么状态？
	有历史购物车，怎么应用新的价格表，非要在购物车中修改吗？
	销售团队负责那些电商网站？
	所有后台的去网站都改为新窗口
	product.category 扩展一个排序字段


	产品生命周期管理
	PLM, 企业版才有
	这个和产品管理应该区别对待，PLM重点在产品设计，产品规划，产品开发等整个生命周期管理，后者应该对接，而不是集成为一个产品
	关于product模块的思考
	是否应该尽量遵从odoo的模块体系。product模块在odoo中属于基础模块，促销基于sale_management
	odoo中，sale间接基于product， anodoo_prod 应该包装成Anodoo Product产品。产品价格表属于产品，不单独（因为odoo中是在一起的），产品推荐作为营销里，产品促销属于销售领域


	实体
	Product.category
	product.template 产品模板，如果没有属性，也会创建一个一对一的product对象，包括一个多个产品变体。
	Product.product 产品,具有属性的产品
	
	Product.packaging  产品包。在产品变体上维护。当一个产品只有一个变体时，可以在产品模板中编辑。实际上是在变体上维护
	Product.supplierinfo
	在product.template 中定义了如下两个字段。 在安装了采购模块时，会在产品的采购页签中显示。
seller_ids = fields.One2many('product.supplierinfo', 'product_tmpl_id', 'Vendors', help="Define vendor pricelists.")
	    variant_seller_ids = fields.One2many('product.supplierinfo', 'product_tmpl_id')
	
	
	product.attribute 产品属性,给产品模板使用来定义产品的
	product.attribute.value 产品属性值
	
	product.template.attribute.line
	product.template.attribute.value
	product.template.attribute.exclusion
	
	product.pricelist
	product.pricelist.item
	扩展
	Res.partner : 客户特定价格表


信息
	barcode
	type = fields.Selection([
        ('consu', 'Consumable'),
        ('service', 'Service')],
	其中：A storable product is a product for which you manage stock. The Inventory app has to be installed.
	其中：product可能是预留的
	图片
	货币
	单位
变体
	变体的创建，创建模式有三种：即时，动态，从不
	没有变体属性时的创建：自动创建
	互斥的属性设置和显示：可选附件是基于产品变体的，所以可以通过属性来互斥。而替代产品是基于产品模板的，不能使用属性来互斥。可选产品则是在加入购物车里再选择属性，当互斥的属性时无法选择。
	product.product和product.template的关系。是继承关系。
	class ProductProduct(models.Model):
    _name = "product.product"
    _description = "Product"
    _inherits = {'product.template': 'product_tmpl_id'}

产品模板
	搜索：product.template.search
	列表：product.template.product.tree
	form：product.template.product.form，继承自：product.template.common.form
产品变体
	列表：product.product.tree
	搜索：product.product.search 继承自product.template.search

价格的计算
# price: total price, context dependent (partner, pricelist, quantity)
# price_extra: catalog extra value only, sum of variant extra attributes
# lst_price: catalog value + extra, context dependent (uom)
standard_price：成本，不同批次进货价格不同，如何体现在成本里？





供应商信息
	
	有action，但是在purchase模块放开：product.product_supplierinfo_type_action

产品包
	有action，但是在stock模块放开：product.action_packaging_view

客户特定价格表

演示
accessory_product_ids
consu_delivery_01
1.1.1.1.	Product_matrix
	依赖
	Account
	扩展product,实现产品的matrix模式
1.1.1.2.	sale_product_matrix
	功能
	快速选报价
	依赖
	Sale, product_matrix, sale_product_configurator
'''

documents_product
开启集中的产品文档管理，但好像在产品中看不到其所属的文档（后续增强）
