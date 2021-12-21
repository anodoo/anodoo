# -*- coding: utf-8 -*-
{
    'name': "模块体系",

    'summary': """
        Anodoo模块体系管理
    """,

    'description': """
        Anodoo模块体系管理
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
        'security/base_module_security.xml',
        'security/ir.model.access.csv',

        'data/base_module_data.xml',

        'views/base_module_views.xml',
        'views/base_module_analysis_views.xml',
        'views/base_module_menu.xml',
        'views/base_module_templates.xml',
    ],

    'demo': [
        'demo/base_module_demo.xml',
    ],
}