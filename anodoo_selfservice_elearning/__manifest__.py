# -*- coding: utf-8 -*-
{
    'name': "自助服务在线学习",

    'summary': """
        为客户自助服务平台增加在线学习功能
    """,

    'description': """
        为客户自助服务平台增加在线学习功能
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-selfservice",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,
    'auto_install': True,

    'depends': [
        'website_slides',
        'anodoo_selfservice'
    ],

    'data': [
        'data/selfservice_elearning_data.xml',
        'security/selfservice_elearning_security.xml',
        'security/ir.model.access.csv',
        'views/selfservice_elearning_views.xml',
        'views/res_config_settings_views.xml',
        'views/selfservice_elearning_menu.xml',
        'views/selfservice_elearning_templates.xml',
    ],

    'demo': [
        'demo/selfservice_elearning_demo.xml',
    ],
}