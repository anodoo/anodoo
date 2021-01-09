# -*- coding: utf-8 -*-
{
    'name': "quality",

    'summary': """
        quality
    """,

    'description': """
        quality
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-quality",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/quality_security.xml',
        'security/ir.model.access.csv',

        'data/quality_data.xml',

        'views/quality_views.xml',
        'views/quality_analysis_views.xml',
        'views/quality_menu.xml',
        'views/quality_templates.xml',
    ],

    'demo': [
        'demo/quality_demo.xml',
    ],
}