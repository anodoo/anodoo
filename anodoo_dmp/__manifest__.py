# -*- coding: utf-8 -*-
{
    'name': "dmp",

    'summary': """
        dmp
    """,

    'description': """
        dmp
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-dmp",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/dmp_security.xml',
        'security/ir.model.access.csv',

        'data/dmp_data.xml',

        'views/dmp_views.xml',
        'views/dmp_analysis_views.xml',
        'views/dmp_menu.xml',
        'views/dmp_templates.xml',
    ],

    'demo': [
        'demo/dmp_demo.xml',
    ],
}