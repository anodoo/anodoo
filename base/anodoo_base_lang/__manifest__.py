# -*- coding: utf-8 -*-
{
    'name': "语言",

    'summary': """
        语言设置，多语言支持
    """,

    'description': """
        语言设置，多语言支持
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-base",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': ['base'],

    'data': [
        'security/base_lang_security.xml',
        'security/ir.model.access.csv',

        'data/base_lang_data.xml',

        'views/base_lang_views.xml',
        'views/base_lang_analysis_views.xml',
        'views/base_lang_menu.xml',
        'views/base_lang_templates.xml',
    ],

    'demo': [
        'demo/base_lang_demo.xml',
    ],
}