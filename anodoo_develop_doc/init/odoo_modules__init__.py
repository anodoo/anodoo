# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

""" Modules (also called addons) management.

"""

from . import db, graph, loading, migration, module, registry

from odoo.modules.loading import load_modules, reset_modules_state

from odoo.modules.module import (
    adapt_version,
    get_module_path,
    get_module_resource,
    get_modules,
    get_modules_with_version,
    get_resource_from_path,
    get_resource_path,
    initialize_sys_path,
    load_information_from_description_file,
    load_openerp_module,
)

#odoo.modules.module.load_openerp_module(m)
#   load_information_from_description_file(module_name)  load 模块的__manifest__.py
#       好像只load 信息而已,而且，web比base早
#   post_load 好像没有找到相应的方法，在laod完进行的操作。

#class Registry(Mapping):
#是一个map，一个数据库name，map一个,其中这个map是一个LRU的cache，参考tools.lru.py
#registry = object.__new__(cls)
#                registry.init(db_name)

#loading.py  最关键的load模块  里面都是几个重要的load方法： load_modules
#

#db.py
#is_initialized ,Check if a database has been initialized for the ORM.  根据table_exists(cr, 'ir_module_module')
#initialize   了解base_data.sql

#Graph(dict):    """ Modules dependency graph.  里面实质上是一个dict对象，将所有module的depend关系进行维护
# add_module 是主要方法，

#pre_init_hook  在首次load模块时使用

#load的层次，首先是python层，然后是register层

'''
				1. Module.py
l Odoo的anodoo中的各个module
l Hook
l Unittest  参考标准库中的开发工具部分

l  
l  
				2. Registry.py
l 就是一个Mapping对象
l 针对不同数据库有一个registry
l 有一个lock，cache机制
	n 参考odoo.tools.LRU
l 机制
	n New
l _new_
l Init
l 调用load_modules  L85
	n Load一个module就装载到Graph中
	n Setup_models
l 注册所有的model
    L222:for cls in models.MetaModel.module_to_models.get(module.name, []):
    model = cls._build_model(self, cr) :根据model的继承关系，调用__new__,__init__最终创建了一个model的实例
    setup_models 安装model的所有信息，包括field，trigger等
        
				3. Loading.py
l Load_modules函数 L320
	n 先load base模块，setup
Load其他模块


module的几种状态
uninstallable  不可安装
uninstalled    未安装
to install     安装中
to upgrade   升级中
installed       已安装
'''