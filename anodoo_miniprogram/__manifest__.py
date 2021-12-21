# -*- coding: utf-8 -*-
{
    'name': "miniprogram",

    'summary': """
        miniprogram
    """,

    'description': """
        miniprogram
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-miniprogram",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/miniprogram_security.xml',
        'security/ir.model.access.csv',

        'data/miniprogram_data.xml',

        'views/miniprogram_views.xml',
        'views/miniprogram_analysis_views.xml',
        'views/miniprogram_menu.xml',
        'views/miniprogram_templates.xml',
    ],

    'demo': [
        'demo/miniprogram_demo.xml',
    ],
}