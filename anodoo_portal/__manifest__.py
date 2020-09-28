# -*- coding: utf-8 -*-
{
    'name': "portal",

    'summary': """
        portal
    """,

    'description': """
        portal
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-portal",


    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    'depends': [
        'portal',

    ],

    'data': [
        'security/portal_security.xml',
        'security/ir.model.access.csv',

        'data/portal_data.xml',

        'views/portal_views.xml',
        'views/portal_analysis_views.xml',
        'views/portal_menu.xml',
        'views/portal_templates.xml',
    ],

    'demo': [
        'demo/portal_demo.xml',
    ],
}