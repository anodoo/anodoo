# -*- coding: utf-8 -*-
{
    'name': "产品管理",

    'summary': """
        产品管理
    """,

    'description': """
        实现产品管理,产品价格,产品促销,产品推荐
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-product",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'product',
    ],

    # always loaded
    'data': [
        'data/product_data.xml',
        'security/product_security.xml',
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/res_config_settings_views.xml',
        'views/product_menu.xml',
        'views/product_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/product_demo.xml'],
}