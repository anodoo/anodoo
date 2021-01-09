# -*- coding: utf-8 -*-
{
    'name': "h5",

    'summary': """
        h5
    """,

    'description': """
        h5
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-h5",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/h5_security.xml',
        'security/ir.model.access.csv',

        'data/h5_data.xml',

        'views/h5_views.xml',
        'views/h5_analysis_views.xml',
        'views/h5_menu.xml',
        'views/h5_templates.xml',
    ],

    'demo': [
        'demo/h5_demo.xml',
    ],
}