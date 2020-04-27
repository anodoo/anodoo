# -*- coding: utf-8 -*-
{
    'name': "发票",

    'summary': """
        发票管理
    """,

    'description': """
        发票管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-invoice",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,
    'auto_install': True,

    # any module necessary for this one to work correctly
    'depends': ['sale', 'account', 'product_margin',
                'anodoo_sfa'],

    # always loaded
    'data': [
        'data/invoice_data.xml',
        #'demo/demo.xml',#demo
        'security/invoice_security.xml',
        'security/ir.model.access.csv',
        'views/invoice_views.xml',
        'views/invoice_menu.xml',
        'views/invoice_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/demo.xml',],
}