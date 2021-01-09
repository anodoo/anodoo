# -*- coding: utf-8 -*-
{
    'name': "配送",

    'summary': """
        订单配送
    """,

    'description': """
        订单配送
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-delivery",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'delivery'
    ],

    'data': [
        'security/delivery_security.xml',
        'security/ir.model.access.csv',

        'data/delivery_data.xml',

        'views/res_config_settings_views.xml',
        'views/delivery_views.xml',
        'views/delivery_analysis_views.xml',
        'views/delivery_menu.xml',
        'views/delivery_templates.xml',
    ],

    'demo': [
        'demo/delivery_demo.xml',
    ],
}