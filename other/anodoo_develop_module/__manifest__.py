# -*- coding: utf-8 -*-
{
    'name': "开发工具-模块结构",

    'summary': """
        开发工具-模块结构
    """,

    'description': """
        开发工具-模块结构
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-develop",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'base'
    ],

    'data': [
        'security/develop_module_security.xml',
        'security/ir.model.access.csv',

        'data/develop_module_data.xml',

        'views/develop_module_views.xml',
        'views/develop_module_analysis_views.xml',
        'views/develop_module_menu.xml',
        'views/develop_module_templates.xml',
    ],

    'demo': [
        'demo/develop_module_demo.xml',
    ],
}