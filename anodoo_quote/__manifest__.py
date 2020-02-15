# -*- coding: utf-8 -*-
{
    'name': "报价",

    'summary': """
        报价管理
    """,

    'description': """
        报价管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-quote",

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
        'data/quote_data.xml',
        'security/quote_security.xml',
        'security/ir.model.access.csv',
        'views/quote_views.xml',
        'views/quote_menu.xml',
        'views/quote_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/quote_demo.xml',
    ],
}