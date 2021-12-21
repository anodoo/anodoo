# -*- coding: utf-8 -*-
{
    'name': "OAuth扩展",

    'summary': """
        OAuth扩展
    """,

    'description': """
        OAuth扩展
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-auth",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'auth_oauth',
    ],

    'data': [
        'security/auth_oauth_security.xml',
        'security/ir.model.access.csv',

        'data/auth_oauth_data.xml',

        'views/auth_oauth_views.xml',
        'views/auth_oauth_analysis_views.xml',
        'views/auth_oauth_menu.xml',
        'views/auth_oauth_templates.xml',
    ],

    'demo': [
        'demo/auth_oauth_demo.xml',
    ],
}