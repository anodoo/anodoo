# -*- coding: utf-8 -*-
{
    'name': "会员销售",

    'summary': """
        会员销售
    """,

    'description': """
        会员销售
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-membership",


    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    'depends': [
        'membership'
    ],

    'data': [
        'security/membership_security.xml',
        'security/ir.model.access.csv',

        'data/membership_data.xml',

        'views/membership_views.xml',
        'views/membership_analysis_views.xml',
        'views/membership_menu.xml',
        'views/membership_templates.xml',
    ],

    'demo': [
        'demo/membership_demo.xml',
    ],
}