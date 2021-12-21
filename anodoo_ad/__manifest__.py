# -*- coding: utf-8 -*-
{
    'name': "ad",

    'summary': """
        ad
    """,

    'description': """
        ad
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-ad",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/ad_security.xml',
        'security/ir.model.access.csv',

        'data/ad_data.xml',

        'views/ad_views.xml',
        'views/ad_analysis_views.xml',
        'views/ad_menu.xml',
        'views/ad_templates.xml',
    ],

    'demo': [
        'demo/ad_demo.xml',
    ],
}