# -*- coding: utf-8 -*-
{
    'name': "cem",

    'summary': """
        cem
    """,

    'description': """
        cem
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-cem",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/cem_security.xml',
        'security/ir.model.access.csv',

        'data/cem_data.xml',

        'views/cem_views.xml',
        'views/cem_analysis_views.xml',
        'views/cem_menu.xml',
        'views/cem_templates.xml',
    ],

    'demo': [
        'demo/cem_demo.xml',
    ],
}