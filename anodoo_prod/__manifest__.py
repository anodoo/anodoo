# -*- coding: utf-8 -*-
{
    'name': "Anodoo PM",

    'summary': """
        Product Marketing, 实现产品管理,产品价格,产品促销,产品推荐
    """,

    'description': """
        实现产品管理,产品价格,产品促销,产品推荐
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-prod",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['product',
                'anodoo_base',],

    # always loaded
    'data': [
        'data/prod_data.xml',
        #'demo/demo.xml',#demo
        'security/prod_security.xml',
        'security/ir.model.access.csv',
        'views/prod_views.xml',
        'views/product_views.xml',
        'views/res_config_settings_views.xml',
        'views/prod_menu.xml',
        'views/prod_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/demo.xml',],
}