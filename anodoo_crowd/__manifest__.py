# -*- coding: utf-8 -*-
{
    'name': "crowd",

    'summary': """
        crowd
    """,

    'description': """
        crowd
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-crowd",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/crowd_security.xml',
        'security/ir.model.access.csv',

        'data/crowd_data.xml',

        'views/crowd_views.xml',
        'views/crowd_analysis_views.xml',
        'views/crowd_menu.xml',
        'views/crowd_templates.xml',
    ],

    'demo': [
        'demo/crowd_demo.xml',
    ],
}