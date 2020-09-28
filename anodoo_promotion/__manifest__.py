# -*- coding: utf-8 -*-
{
    'name': "促销",

    'summary': """
        促销
    """,

    'description': """
        促销
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-promotion",


    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    'depends': [
        'sale_coupon',
    ],

    'data': [
        'security/promotion_security.xml',
        'security/ir.model.access.csv',

        'data/promotion_data.xml',

        'views/promotion_views.xml',
        'views/promotion_analysis_views.xml',
        'views/promotion_menu.xml',
        'views/promotion_templates.xml',
    ],

    'demo': [
        'demo/promotion_demo.xml',
    ],
}