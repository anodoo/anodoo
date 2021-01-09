# -*- coding: utf-8 -*-

from . import controllers
from . import models


'''

Sale_product_configurator

	依赖
	Sale
	功能
	报价时,选产品
	同时，提供可选产品


Bridge module to make the website e-commerce compatible with the product configurator
'depends': ['website_sale', 'sale_product_configurator']

	功能
	电商web上选配产品
	依赖
	Website_sale
	Sale_product_configurator



'''
