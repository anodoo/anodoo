# -*- coding: utf-8 -*-
{
    'name': "membership",

    'summary': """
        membership
    """,

    'description': """
        membership
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-membership",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/membership_security.xml',
        'security/ir.model.access.csv',

        'data/membership_data.xml',

        'views/membership_views.xml',
        'views/membership_analysis_views.xml',
        'views/membership_menu.xml',
        'views/membership_templates.xml',
    ],

    'demo': [
        'demo/membership_demo.xml',
    ],
}