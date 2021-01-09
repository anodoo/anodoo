# -*- coding: utf-8 -*-
{
    'name': "客户分群",

    'summary': """
        客户分群
    """,

    'description': """
        客户分群
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-customer-segment",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'anodoo_customer',
    ],

    'data': [
        'security/customer_segment_security.xml',
        'security/ir.model.access.csv',

        'data/customer_segment_data.xml',

        'views/customer_segment_views.xml',
        'views/res_partner_views.xml',
        'views/customer_segment_analysis_views.xml',
        'views/customer_segment_menu.xml',
        'views/customer_segment_templates.xml',
    ],

    'demo': [
        'demo/customer_segment_demo.xml',
    ],
}