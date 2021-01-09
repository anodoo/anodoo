# -*- coding: utf-8 -*-
{
    'name': "sfa",

    'summary': """
        sfa
    """,

    'description': """
        sfa
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-sfa",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/sfa_security.xml',
        'security/ir.model.access.csv',

        'data/sfa_data.xml',

        'views/sfa_views.xml',
        'views/sfa_analysis_views.xml',
        'views/sfa_menu.xml',
        'views/sfa_templates.xml',
    ],

    'demo': [
        'demo/sfa_demo.xml',
    ],
}