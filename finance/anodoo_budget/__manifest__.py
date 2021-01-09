# -*- coding: utf-8 -*-
{
    'name': "budget",

    'summary': """
        budget
    """,

    'description': """
        budget
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-budget",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/budget_security.xml',
        'security/ir.model.access.csv',

        'data/budget_data.xml',

        'views/budget_views.xml',
        'views/budget_analysis_views.xml',
        'views/budget_menu.xml',
        'views/budget_templates.xml',
    ],

    'demo': [
        'demo/budget_demo.xml',
    ],
}