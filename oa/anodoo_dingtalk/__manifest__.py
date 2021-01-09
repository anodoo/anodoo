# -*- coding: utf-8 -*-
{
    'name': "dingtalk",

    'summary': """
        dingtalk
    """,

    'description': """
        dingtalk
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-dingtalk",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/dingtalk_security.xml',
        'security/ir.model.access.csv',

        'data/dingtalk_data.xml',

        'views/dingtalk_views.xml',
        'views/dingtalk_analysis_views.xml',
        'views/dingtalk_menu.xml',
        'views/dingtalk_templates.xml',
    ],

    'demo': [
        'demo/dingtalk_demo.xml',
    ],
}