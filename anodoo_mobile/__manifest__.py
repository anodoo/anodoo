# -*- coding: utf-8 -*-
{
    'name': "mobile",

    'summary': """
        mobile
    """,

    'description': """
        mobile
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-mobile",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/mobile_security.xml',
        'security/ir.model.access.csv',

        'data/mobile_data.xml',

        'views/mobile_views.xml',
        'views/mobile_analysis_views.xml',
        'views/mobile_menu.xml',
        'views/mobile_templates.xml',
    ],

    'demo': [
        'demo/mobile_demo.xml',
    ],
}