# -*- coding: utf-8 -*-
{
    'name': "srm",

    'summary': """
        srm
    """,

    'description': """
        srm
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-srm",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/srm_security.xml',
        'security/ir.model.access.csv',

        'data/srm_data.xml',

        'views/srm_views.xml',
        'views/srm_analysis_views.xml',
        'views/srm_menu.xml',
        'views/srm_templates.xml',
    ],

    'demo': [
        'demo/srm_demo.xml',
    ],
}