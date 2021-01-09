# -*- coding: utf-8 -*-
{
    'name': "品牌标示",

    'summary': """
        品牌标示，去Odoo品牌标示等
    """,

    'description': """
        品牌标示，去Odoo品牌标示等
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-base",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'base'
    ],

    'data': [
        'security/base_branding_security.xml',
        'security/ir.model.access.csv',

        'data/base_branding_data.xml',

        'views/base_branding_views.xml',
        'views/base_branding_analysis_views.xml',
        'views/base_branding_menu.xml',
        'views/base_branding_templates.xml',
    ],

    'demo': [
        'demo/base_branding_demo.xml',
    ],
}