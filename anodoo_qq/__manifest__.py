# -*- coding: utf-8 -*-
{
    'name': "qq",

    'summary': """
        qq
    """,

    'description': """
        qq
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-qq",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/qq_security.xml',
        'security/ir.model.access.csv',

        'data/qq_data.xml',

        'views/qq_views.xml',
        'views/qq_analysis_views.xml',
        'views/qq_menu.xml',
        'views/qq_templates.xml',
    ],

    'demo': [
        'demo/qq_demo.xml',
    ],
}