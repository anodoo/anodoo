# -*- coding: utf-8 -*-
{
    'name': "enabling",

    'summary': """
        enabling
    """,

    'description': """
        enabling
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-enabling",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/enabling_security.xml',
        'security/ir.model.access.csv',

        'data/enabling_data.xml',

        'views/enabling_views.xml',
        'views/enabling_analysis_views.xml',
        'views/enabling_menu.xml',
        'views/enabling_templates.xml',
    ],

    'demo': [
        'demo/enabling_demo.xml',
    ],
}