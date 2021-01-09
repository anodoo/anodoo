# -*- coding: utf-8 -*-
{
    'name': "商城",

    'summary': """
        多店铺的商城平台
    """,

    'description': """
        多店铺的商城平台
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-marketplace",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/marketplace_security.xml',
        'security/ir.model.access.csv',

        'data/marketplace_data.xml',

        'views/marketplace_views.xml',
        'views/marketplace_analysis_views.xml',
        'views/marketplace_menu.xml',
        'views/marketplace_templates.xml',
    ],

    'demo': [
        'demo/marketplace_demo.xml',
    ],
}