# -*- coding: utf-8 -*-
{
    'name': "aftersale",

    'summary': """
        aftersale
    """,

    'description': """
        aftersale
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-aftersale",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/aftersale_security.xml',
        'security/ir.model.access.csv',

        'data/aftersale_data.xml',

        'views/aftersale_views.xml',
        'views/aftersale_analysis_views.xml',
        'views/aftersale_menu.xml',
        'views/aftersale_templates.xml',
    ],

    'demo': [
        'demo/aftersale_demo.xml',
    ],
}