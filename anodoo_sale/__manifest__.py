# -*- coding: utf-8 -*-
{
    'name': "销售管理",

    'summary': """
        销售管理
    """,

    'description': """
        销售管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-sale",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base', 'anodoo_team', 'anodoo_proj'],

    # always loaded
    'data': [
        'data/sale_data.xml',
        'security/sale_security.xml',
        'security/ir.model.access.csv',
        'views/sale_views.xml',
        'views/sale_menu.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}