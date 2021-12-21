# -*- coding: utf-8 -*-
{
    'name': "recommend",

    'summary': """
        recommend
    """,

    'description': """
        recommend
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-recommend",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/recommend_security.xml',
        'security/ir.model.access.csv',

        'data/recommend_data.xml',

        'views/recommend_views.xml',
        'views/recommend_analysis_views.xml',
        'views/recommend_menu.xml',
        'views/recommend_templates.xml',
    ],

    'demo': [
        'demo/recommend_demo.xml',
    ],
}