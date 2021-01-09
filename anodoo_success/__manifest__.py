# -*- coding: utf-8 -*-
{
    'name': "success",

    'summary': """
        success
    """,

    'description': """
        success
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-success",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/success_security.xml',
        'security/ir.model.access.csv',

        'data/success_data.xml',

        'views/success_views.xml',
        'views/success_analysis_views.xml',
        'views/success_menu.xml',
        'views/success_templates.xml',
    ],

    'demo': [
        'demo/success_demo.xml',
    ],
}