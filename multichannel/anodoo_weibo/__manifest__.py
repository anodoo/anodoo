# -*- coding: utf-8 -*-
{
    'name': "weibo",

    'summary': """
        weibo
    """,

    'description': """
        weibo
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-weibo",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/weibo_security.xml',
        'security/ir.model.access.csv',

        'data/weibo_data.xml',

        'views/weibo_views.xml',
        'views/weibo_analysis_views.xml',
        'views/weibo_menu.xml',
        'views/weibo_templates.xml',
    ],

    'demo': [
        'demo/weibo_demo.xml',
    ],
}