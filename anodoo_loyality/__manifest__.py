# -*- coding: utf-8 -*-
{
    'name': "loyality",

    'summary': """
        loyality
    """,

    'description': """
        loyality
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-loyality",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/loyality_security.xml',
        'security/ir.model.access.csv',

        'data/loyality_data.xml',

        'views/loyality_views.xml',
        'views/loyality_analysis_views.xml',
        'views/loyality_menu.xml',
        'views/loyality_templates.xml',
    ],

    'demo': [
        'demo/loyality_demo.xml',
    ],
}