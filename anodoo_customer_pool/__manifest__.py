# -*- coding: utf-8 -*-
{
    'name': "客户池",

    'summary': """
        客户池
    """,

    'description': """
        客户池
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-customer-pool",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'anodoo_customer',
    ],

    'data': [
        'security/customer_pool_security.xml',
        'security/ir.model.access.csv',

        'data/customer_pool_data.xml',

        'views/customer_pool_views.xml',
        'views/res_partner_views.xml',
        'views/customer_pool_analysis_views.xml',
        'views/customer_pool_menu.xml',
        'views/customer_pool_templates.xml',
    ],

    'demo': [
        'demo/customer_pool_demo.xml',
    ],
}