# -*- coding: utf-8 -*-
{
    'name': "销售区域",

    'summary': """
        销售区域
    """,

    'description': """
        销售区域
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-territory",


    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    'depends': [
        'anodoo_sales',
    ],

    'data': [
        'security/territory_security.xml',
        'security/ir.model.access.csv',

        'data/territory_data.xml',

        'views/territory_views.xml',
        'views/territory_analysis_views.xml',
        'views/territory_menu.xml',
        'views/territory_templates.xml',
    ],

    'demo': [
        'demo/territory_demo.xml',
    ],
}