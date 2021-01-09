# -*- coding: utf-8 -*-
{
    'name': "mps",

    'summary': """
        mps
    """,

    'description': """
        mps
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-mps",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/mps_security.xml',
        'security/ir.model.access.csv',

        'data/mps_data.xml',

        'views/mps_views.xml',
        'views/mps_analysis_views.xml',
        'views/mps_menu.xml',
        'views/mps_templates.xml',
    ],

    'demo': [
        'demo/mps_demo.xml',
    ],
}