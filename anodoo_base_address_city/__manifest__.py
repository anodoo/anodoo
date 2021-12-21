# -*- coding: utf-8 -*-
{
    'name': "地址中城市扩展",

    'summary': """
        地址中城市扩展
    """,

    'description': """
        地址中城市扩展
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-base",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'base_address_city',
    ],

    'data': [
        'security/base_address_city_security.xml',
        'security/ir.model.access.csv',

        'data/base_address_city_data.xml',

        'views/base_address_city_views.xml',
        'views/base_address_city_analysis_views.xml',
        'views/base_address_city_menu.xml',
        'views/base_address_city_templates.xml',
    ],

    'demo': [
        'demo/base_address_city_demo.xml',
    ],
}