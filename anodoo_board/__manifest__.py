# -*- coding: utf-8 -*-
{
    'name': "仪表盘",

    'summary': """
        仪表盘
    """,

    'description': """
        仪表盘
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-board",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'board'
    ],

    # always loaded
    'data': [
        'data/board_data.xml',
        'security/board_security.xml',
        'security/ir.model.access.csv',
        'views/board_views.xml',
        'views/board_menu.xml',
        'views/board_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/board_demo.xml',
    ],
}