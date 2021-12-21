# -*- coding: utf-8 -*-
{
    'name': "银行管理",

    'summary': """
        银行管理的扩展
    """,

    'description': """
        base_bank
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-base-bank",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/base_bank_security.xml',
        'security/ir.model.access.csv',

        'data/base_bank_data.xml',

        'views/base_bank_views.xml',
        'views/base_bank_analysis_views.xml',
        'views/base_bank_menu.xml',
        'views/base_bank_templates.xml',
    ],

    'demo': [
        'demo/base_bank_demo.xml',
    ],
}