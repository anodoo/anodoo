# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models
from . import wizard


'''

delivery	***	交货成本	交货	FALSE	FALSE	sale_stock , sale_management , 
企业版：	delivery_barcode	*	交货条形码扫描	交货	TRUE	FALSE	stock_barcode , delivery , 

以下均为各种物流的集成
	delivery_bpost	-1	bpost运输	交货	FALSE	TRUE	delivery , mail , 
	delivery_dhl	-1	DHL 快递	交货	FALSE	TRUE	delivery , mail , 
	delivery_easypost	-1	Easypost 物流	交货	FALSE	TRUE	delivery , mail , 
	delivery_fedex	-1	联邦航运	交货	FALSE	TRUE	delivery , mail , 
	delivery_ups	-1	UPS 发货	交货	FALSE	TRUE	delivery , mail , 
	delivery_usps	-1	美国邮政(USPS)货运	交货	FALSE	TRUE	delivery , mail , 


实体
delivery.carrier  一个物流商，包括免费，ups，顺丰等
    不同的物流商如何扩展，参考这里的说明
    可以设置这个物流商支持配送到哪里？哪个国家，省份等
    
delivery.price.rule  基于物流网格，设置不同区域的不同价格

product.packaging 借用product模块的对象。一方面作为产品的包裹包装如一箱奶等，一方面在物流中作为一个特定的包裹箱，如一个30*50*100的箱子。


'''
