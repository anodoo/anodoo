# -*- coding: utf-8 -*-
{
    'name': "mes",

    'summary': """
        mes
    """,

    'description': """
        mes
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-mes",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/mes_security.xml',
        'security/ir.model.access.csv',

        'data/mes_data.xml',

        'views/mes_views.xml',
        'views/mes_analysis_views.xml',
        'views/mes_menu.xml',
        'views/mes_templates.xml',
    ],

    'demo': [
        'demo/mes_demo.xml',
    ],
}