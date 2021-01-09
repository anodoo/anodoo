# -*- coding: utf-8 -*-
{
    'name': "order",

    'summary': """
        order
    """,

    'description': """
        order
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-order",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/order_security.xml',
        'security/ir.model.access.csv',

        'data/order_data.xml',

        'views/order_views.xml',
        'views/order_analysis_views.xml',
        'views/order_menu.xml',
        'views/order_templates.xml',
    ],

    'demo': [
        'demo/order_demo.xml',
    ],
}