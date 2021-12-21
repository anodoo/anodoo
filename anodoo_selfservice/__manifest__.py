# -*- coding: utf-8 -*-
{
    'name': "自助服务",

    'summary': """
        自助服务网站
    """,

    'description': """
        自助服务网站
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-selfservice",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'website',
    ],

    # always loaded
    'data': [
        'data/selfservice_data.xml',
        'security/selfservice_security.xml',
        'security/ir.model.access.csv',
        'views/selfservice_views.xml',
        'views/res_config_settings_views.xml',
        'views/selfservice_menu.xml',
        'views/selfservice_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/selfservice_demo.xml',
    ],
}