# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models
from . import report
from . import wizard


def post_init(cr, registry):
    """Rewrite ICP's to force groups"""
    from odoo import api, SUPERUSER_ID

    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.config_parameter'].init(force=True)

'''
相关模块

base			*	基础	技术设置			TRUE	FALSE	

base_address_city	*	城市地址	工具			FALSE	FALSE	base , 
	扩展了城市的地址，比较有用。
base_address_extended	*	扩展地址	技术设置		FALSE	FALSE	base , 	
	地址格式化，比较有用。

base_automation		*	自动动作规则	销售			FALSE	FALSE	base , resource , mail , 
	很有用的模块。	为一些记录，根据不同的条件出发自动动作，如一个lead，创建3天后，检查完成状态，没有完成则提醒。

base_setup		*	初始化设置工具	技术设置		FALSE	FALSE	base , web , 
	很有用，General Settings的功能，所有继承General Settings，都应该用这个

	base_gengo		*	通过 Gengo API 自动翻译	工具		FALSE	FALSE	base_setup , 
	base_geolocalize	*	业务伙伴地理定位	工具		FALSE	FALSE	base_setup , 

base_import		*	基础导入	工具			TRUE	FALSE	web , 
base_import_module	*	基础导入 模块	工具			FALSE	FALSE	web , 
	导入文件内容等

base_sparse_field	*	稀疏字段	技术设置		FALSE	FALSE	base , 

base_vat		*	增值税号码验证	会计			FALSE	FALSE	account , 
base_iban		*	IBAN银行账号	工具			FALSE	FALSE	account , web , 

企业版
base_automation_hr_contract	*	基于员工合同的自动操作	人力资源		TRUE	FALSE	base_automation , hr_contract , 

'''
