# -*- coding: utf-8 -*-
{
    'name': "service",

    'summary': """
        service
    """,

    'description': """
        service
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-service",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/service_security.xml',
        'security/ir.model.access.csv',

        'data/service_data.xml',

        'views/service_views.xml',
        'views/service_analysis_views.xml',
        'views/service_menu.xml',
        'views/service_templates.xml',
    ],

    'demo': [
        'demo/service_demo.xml',
    ],
}