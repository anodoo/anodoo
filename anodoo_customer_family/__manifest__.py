# -*- coding: utf-8 -*-
{
    'name': "家庭客户",

    'summary': """
        家庭客户
    """,

    'description': """
        家庭客户
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-customer-family",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'anodoo_customer',
    ],

    'data': [
        'security/customer_family_security.xml',
        'security/ir.model.access.csv',

        'data/customer_family_data.xml',

        'views/customer_family_views.xml',
        'views/res_partner_views.xml',
        'views/customer_family_analysis_views.xml',
        'views/customer_family_menu.xml',
        'views/customer_family_templates.xml',
    ],

    'demo': [
        'demo/customer_family_demo.xml',
    ],
}