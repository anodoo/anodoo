# -*- coding: utf-8 -*-
{
    'name': "IAP",

    'summary': """
        IAP，In App Purchase
    """,

    'description': """
        IAP，In App Purchase
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-iap",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/iap_security.xml',
        'security/ir.model.access.csv',

        'data/iap_data.xml',

        'views/iap_views.xml',
        'views/iap_analysis_views.xml',
        'views/iap_menu.xml',
        'views/iap_templates.xml',
    ],

    'demo': [
        'demo/iap_demo.xml',
    ],
}