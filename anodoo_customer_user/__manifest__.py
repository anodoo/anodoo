# -*- coding: utf-8 -*-
{
    'name': "客户下的用户管理",

    'summary': """
        客户下的用户管理
    """,

    'description': """
        客户下的用户管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-customer-user",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'anodoo_customer',
    ],

    'data': [
        'security/customer_user_security.xml',
        'security/ir.model.access.csv',

        'data/customer_user_data.xml',

        'views/customer_user_views.xml',
        'views/customer_user_analysis_views.xml',
        'views/customer_user_menu.xml',
        'views/customer_user_templates.xml',
    ],

    'demo': [
        'demo/customer_user_demo.xml',
    ],
}