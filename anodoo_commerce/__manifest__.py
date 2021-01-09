# -*- coding: utf-8 -*-
{
    'name': "commerce",

    'summary': """
        commerce
    """,

    'description': """
        commerce
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-commerce",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

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

    'data': [
        'security/commerce_security.xml',
        'security/ir.model.access.csv',

        'data/commerce_data.xml',

        'views/commerce_views.xml',
        'views/commerce_analysis_views.xml',
        'views/res_config_settings_views.xml',
        'views/commerce_menu.xml',
        'views/commerce_templates.xml',
    ],

    'demo': [
        'demo/commerce_demo.xml',
    ],
}