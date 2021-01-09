# -*- coding: utf-8 -*-
{
    'name': "lunch",

    'summary': """
        lunch
    """,

    'description': """
        lunch
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-lunch",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/lunch_security.xml',
        'security/ir.model.access.csv',

        'data/lunch_data.xml',

        'views/lunch_views.xml',
        'views/lunch_analysis_views.xml',
        'views/lunch_menu.xml',
        'views/lunch_templates.xml',
    ],

    'demo': [
        'demo/lunch_demo.xml',
    ],
}