# -*- coding: utf-8 -*-
{
    'name': "应用市场",

    'summary': """
        应用市场
    """,

    'description': """
        应用市场
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-store",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/store_security.xml',
        'security/ir.model.access.csv',

        'data/store_data.xml',

        'views/store_views.xml',
        'views/store_analysis_views.xml',
        'views/store_menu.xml',
        'views/store_templates.xml',
    ],

    'demo': [
        'demo/store_demo.xml',
    ],
}