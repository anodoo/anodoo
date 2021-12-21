# -*- coding: utf-8 -*-
{
    'name': "自助服务论坛",

    'summary': """
        自助服务和论坛的连接
    """,

    'description': """
        自助服务和论坛的连接
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-selfservice",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,
    'auto_install': True,

    'depends': [
        'website_forum',
        'anodoo_selfservice',
    ],

    'data': [
        'data/selfservice_forum_data.xml',
        'security/selfservice_forum_security.xml',
        'security/ir.model.access.csv',
        'views/selfservice_forum_views.xml',
        'views/res_config_settings_views.xml',
        'views/selfservice_forum_menu.xml',
        'views/selfservice_forum_templates.xml',
    ],

    'demo': [
        'demo/selfservice_forum_demo.xml',
    ],
}