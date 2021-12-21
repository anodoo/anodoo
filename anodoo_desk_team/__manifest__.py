# -*- coding: utf-8 -*-
{
    'name': "服务台团队",

    'summary': """
        商机管理
    """,

    'description': """
        商机管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-desk",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [

        # 'resource',
        'anodoo_team',
        'anodoo_desk'
    ],

    # always loaded
    'data': [
        'data/desk_team_data.xml',
        'security/desk_team_security.xml',
        'security/ir.model.access.csv',
        'views/desk_ticket_views.xml',
        'views/assets.xml',
        'views/desk_team_views.xml',
        'views/desk_team_analysis_views.xml',
        'views/desk_team_menu.xml',
        'views/desk_team_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/desk_team_demo.xml',
    ]
}