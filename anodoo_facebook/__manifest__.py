# -*- coding: utf-8 -*-
{
    'name': "facebook",

    'summary': """
        facebook
    """,

    'description': """
        facebook
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-facebook",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/facebook_security.xml',
        'security/ir.model.access.csv',

        'data/facebook_data.xml',

        'views/facebook_views.xml',
        'views/facebook_analysis_views.xml',
        'views/facebook_menu.xml',
        'views/facebook_templates.xml',
    ],

    'demo': [
        'demo/facebook_demo.xml',
    ],
}