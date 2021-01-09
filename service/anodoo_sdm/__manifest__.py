# -*- coding: utf-8 -*-
{
    'name': "sdm",

    'summary': """
        sdm
    """,

    'description': """
        sdm
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-sdm",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/sdm_security.xml',
        'security/ir.model.access.csv',

        'data/sdm_data.xml',

        'views/sdm_views.xml',
        'views/sdm_analysis_views.xml',
        'views/sdm_menu.xml',
        'views/sdm_templates.xml',
    ],

    'demo': [
        'demo/sdm_demo.xml',
    ],
}