# -*- coding: utf-8 -*-
{
    'name': "Anodoo Commerce",

    'summary': """
        电子商务
    """,

    'description': """
        电子商务
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-ecomm",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['website_sale',
                'anodoo_base'],

    # always loaded
    'data': [
        'data/ecomm_data.xml',
        'security/ecomm_security.xml',
        'security/ir.model.access.csv',
        'views/ecomm_views.xml',
        'views/ecomm_menu.xml',
        'views/ecomm_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/ecomm_demo.xml',],
}