# -*- coding: utf-8 -*-
{
    'name': "twitter",

    'summary': """
        twitter
    """,

    'description': """
        twitter
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-twitter",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/twitter_security.xml',
        'security/ir.model.access.csv',

        'data/twitter_data.xml',

        'views/twitter_views.xml',
        'views/twitter_analysis_views.xml',
        'views/twitter_menu.xml',
        'views/twitter_templates.xml',
    ],

    'demo': [
        'demo/twitter_demo.xml',
    ],
}