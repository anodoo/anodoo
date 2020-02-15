# -*- coding: utf-8 -*-
{
    'name': "商机",

    'summary': """
        商机管理
    """,

    'description': """
        商机管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-oppor",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base', 'anodoo_sale', 'anodoo_lead'],

    # always loaded
    'data': [
        'data/oppor_data.xml',
        'security/oppor_security.xml',
        'security/ir.model.access.csv',
        'views/oppor_views.xml',
        'views/oppor_menu.xml',
        'views/oppor_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/oppor_demo.xml',
    ],
}