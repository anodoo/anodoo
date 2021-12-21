# -*- coding: utf-8 -*-
{
    'name': "visit",

    'summary': """
        visit
    """,

    'description': """
        visit
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-visit",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/visit_security.xml',
        'security/ir.model.access.csv',

        'data/visit_data.xml',

        'views/visit_views.xml',
        'views/visit_analysis_views.xml',
        'views/visit_menu.xml',
        'views/visit_templates.xml',
    ],

    'demo': [
        'demo/visit_demo.xml',
    ],
}