# -*- coding: utf-8 -*-
{
    'name': "电子商务",

    'summary': """
        电子商务
    """,

    'description': """
        电子商务
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-b2c",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'sales_team',  #以下依赖要从新整理
        'product',
        'sale_coupon',
        'payment',
        'delivery',
        'website_sale',
        'website_sale_comparison',
        'website_sale_stock',
                ],

    # always loaded
    'data': [
        'data/ecommerce_data.xml',
        #'demo/demo.xml',#demo
        'security/ecommerce_security.xml',
        'security/ir.model.access.csv',
        'views/ecommerce_views.xml',
        'views/product_views.xml',
        'views/res_config_settings_views.xml',
        'views/ecommerce_menu.xml',
        'views/ecommerce_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}