# -*- coding: utf-8 -*-
{
    'name': "link",

    'summary': """
        link
    """,

    'description': """
        link
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-link",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'link_tracker', #依赖utm，link_tracker
    ],

    'data': [
        'security/link_security.xml',
        'security/ir.model.access.csv',

        'data/link_data.xml',

        'views/link_views.xml',
        'views/link_analysis_views.xml',
        'views/link_menu.xml',
        'views/link_templates.xml',
    ],

    'demo': [
        'demo/link_demo.xml',
    ],
}