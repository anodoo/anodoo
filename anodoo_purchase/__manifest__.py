# -*- coding: utf-8 -*-
{
    'name': "采购管理",

    'summary': """
        采购管理
    """,

    'description': """
        采购管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-purchase",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'purchase'
    ],

    'data': [
        'security/purchase_security.xml',
        'security/ir.model.access.csv',

        'data/purchase_data.xml',

        'views/purchase_views.xml',
        'views/purchase_analysis_views.xml',
        'views/purchase_menu.xml',
        'views/purchase_templates.xml',
    ],

    'demo': [
        'demo/purchase_demo.xml',
    ],
}