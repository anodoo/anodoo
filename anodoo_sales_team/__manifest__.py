# -*- coding: utf-8 -*-
{
    'name': "销售团队管理",

    'summary': """
        销售团队管理
    """,

    'description': """
        销售团队管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-sales",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'sales_team',
        'anodoo_sales',
    ],

    'data': [
        'security/sales_team_security.xml',
        'security/ir.model.access.csv',

        'data/sales_team_data.xml',

        'views/sales_team_views.xml',
        'views/sales_team_analysis_views.xml',
        'views/sales_team_menu.xml',
        'views/sales_team_templates.xml',
    ],

    'demo': [
        'demo/sales_team_demo.xml',
    ],
}