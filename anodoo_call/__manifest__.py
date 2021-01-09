# -*- coding: utf-8 -*-
{
    'name': "call",

    'summary': """
        call
    """,

    'description': """
        call
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-call",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/call_security.xml',
        'security/ir.model.access.csv',

        'data/call_data.xml',

        'views/call_views.xml',
        'views/call_analysis_views.xml',
        'views/call_menu.xml',
        'views/call_templates.xml',
    ],

    'demo': [
        'demo/call_demo.xml',
    ],
}