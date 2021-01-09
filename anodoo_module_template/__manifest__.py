# -*- coding: utf-8 -*-
{
    'name': "oppor",

    'summary': """
        oppor
    """,

    'description': """
        oppor
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-oppor",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/oppor_security.xml',
        'security/ir.model.access.csv',

        'data/oppor_data.xml',

        'views/oppor_views.xml',
        'views/oppor_analysis_views.xml',
        'views/oppor_menu.xml',
        'views/oppor_templates.xml',
    ],

    'demo': [
        'demo/oppor_demo.xml',
    ],
}