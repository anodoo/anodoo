# -*- coding: utf-8 -*-
{
    'name': "linkedin",

    'summary': """
        linkedin
    """,

    'description': """
        linkedin
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-linkedin",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/linkedin_security.xml',
        'security/ir.model.access.csv',

        'data/linkedin_data.xml',

        'views/linkedin_views.xml',
        'views/linkedin_analysis_views.xml',
        'views/linkedin_menu.xml',
        'views/linkedin_templates.xml',
    ],

    'demo': [
        'demo/linkedin_demo.xml',
    ],
}