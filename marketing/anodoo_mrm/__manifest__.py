# -*- coding: utf-8 -*-
{
    'name': "mrm",

    'summary': """
        mrm
    """,

    'description': """
        mrm
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-mrm",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/mrm_security.xml',
        'security/ir.model.access.csv',

        'data/mrm_data.xml',

        'views/mrm_views.xml',
        'views/mrm_analysis_views.xml',
        'views/mrm_menu.xml',
        'views/mrm_templates.xml',
    ],

    'demo': [
        'demo/mrm_demo.xml',
    ],
}