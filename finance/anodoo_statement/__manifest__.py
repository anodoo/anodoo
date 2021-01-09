# -*- coding: utf-8 -*-
{
    'name': "statement",

    'summary': """
        statement
    """,

    'description': """
        statement
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-statement",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/statement_security.xml',
        'security/ir.model.access.csv',

        'data/statement_data.xml',

        'views/statement_views.xml',
        'views/statement_analysis_views.xml',
        'views/statement_menu.xml',
        'views/statement_templates.xml',
    ],

    'demo': [
        'demo/statement_demo.xml',
    ],
}