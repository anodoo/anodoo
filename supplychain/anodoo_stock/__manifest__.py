# -*- coding: utf-8 -*-
{
    'name': "库存",

    'summary': """
        库存，销售等的基础模块
    """,

    'description': """
        库存，销售等的基础模块
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-stock",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'stock'
    ],

    # always loaded
    'data': [
        'data/stock_data.xml',
        'security/stock_security.xml',
        'security/ir.model.access.csv',
        'views/stock_views.xml',
        'views/stock_menu.xml',
        'views/stock_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/stock_demo.xml',
    ],
}