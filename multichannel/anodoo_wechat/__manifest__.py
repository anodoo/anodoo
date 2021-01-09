# -*- coding: utf-8 -*-
{
    'name': "wechat",

    'summary': """
        wechat
    """,

    'description': """
        wechat
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-wechat",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/wechat_security.xml',
        'security/ir.model.access.csv',

        'data/wechat_data.xml',

        'views/wechat_views.xml',
        'views/wechat_analysis_views.xml',
        'views/wechat_menu.xml',
        'views/wechat_templates.xml',
    ],

    'demo': [
        'demo/wechat_demo.xml',
    ],
}