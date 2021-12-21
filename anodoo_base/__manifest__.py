# -*- coding: utf-8 -*-
{
    'name': "基础",

    'summary': """
        基础模块,这个是对Odoo的架构,base, web等基础模块的扩展, 也是Anodoo的所有应用和模块的基础。
    """,

    'description': """
        Anodoo需要的所有基础功能，对Odoo的所有依赖，对Odoo框架方面的修改都会在此模块中定义。
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'base',
    ],

    # always loaded
    'data': [
        'data/base_data.xml',
        #'demo/demo.xml',#demo
        'security/base_security.xml',
        'security/ir.model.access.csv', 
        #'views/iap_assets.xml',  #iap widget js依赖
        'views/ir_module_views.xml',   
        'views/res_users_views.xml', 
        'views/ir_ui_menu_views.xml',
        
        'views/ir_translation_views.xml',
        'views/base_views.xml',                 
        'views/base_menu.xml',
        'views/base_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}