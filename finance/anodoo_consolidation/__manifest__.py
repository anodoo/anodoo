# -*- coding: utf-8 -*-
{
    'name': "consolidation",

    'summary': """
        consolidation
    """,

    'description': """
        consolidation
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-consolidation",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/consolidation_security.xml',
        'security/ir.model.access.csv',

        'data/consolidation_data.xml',

        'views/consolidation_views.xml',
        'views/consolidation_analysis_views.xml',
        'views/consolidation_menu.xml',
        'views/consolidation_templates.xml',
    ],

    'demo': [
        'demo/consolidation_demo.xml',
    ],
}