# -*- coding: utf-8 -*-
{
    'name': "snailmail",

    'summary': """
        snailmail
    """,

    'description': """
        snailmail
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-snailmail",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/snailmail_security.xml',
        'security/ir.model.access.csv',

        'data/snailmail_data.xml',

        'views/snailmail_views.xml',
        'views/snailmail_analysis_views.xml',
        'views/snailmail_menu.xml',
        'views/snailmail_templates.xml',
    ],

    'demo': [
        'demo/snailmail_demo.xml',
    ],
}