# -*- coding: utf-8 -*-
{
    'name': "content",

    'summary': """
        content
    """,

    'description': """
        content
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-content",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/content_security.xml',
        'security/ir.model.access.csv',

        'data/content_data.xml',

        'views/content_views.xml',
        'views/content_analysis_views.xml',
        'views/content_menu.xml',
        'views/content_templates.xml',
    ],

    'demo': [
        'demo/content_demo.xml',
    ],
}