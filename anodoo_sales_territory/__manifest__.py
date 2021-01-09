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
    'website': "http://www.anodoo.com/module/anodoo-sales-territory",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'anodoo_sales',
    ],

    'data': [
        'security/sales_territory_security.xml',
        'security/ir.model.access.csv',

        'data/sales_territory_data.xml',

        'views/sales_territory_views.xml',
        'views/sales_territory_analysis_views.xml',
        'views/sales_territory_menu.xml',
        'views/sales_territory_templates.xml',
    ],

    'demo': [
        'demo/sales_territory_demo.xml',
    ],
}