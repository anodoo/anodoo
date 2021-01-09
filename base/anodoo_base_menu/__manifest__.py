# -*- coding: utf-8 -*-
{
    'name': "菜单体系",

    'summary': """
        Anodoo菜单体系管理
    """,

    'description': """
        Anodoo菜单体系管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-base",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'base'
    ],

    'data': [
        'security/base_menu_security.xml',
        'security/ir.model.access.csv',

        'data/base_menu_data.xml',

        'views/base_menu_views.xml',
        'views/base_menu_analysis_views.xml',
        'views/base_menu_menu.xml',
        'views/base_menu_templates.xml',
    ],

    'demo': [
        'demo/base_menu_demo.xml',
    ],
}