# -*- coding: utf-8 -*-
{
    'name': "订单",

    'summary': """
        订单管理
    """,

    'description': """
        订单管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-order",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,
    'auto_install': True,

    # any module necessary for this one to work correctly
    'depends': ['sale', 'delivery',
                'anodoo_sfa'],

    # always loaded
    'data': [
        'data/order_data.xml',
        #'demo/demo.xml',#demo
        'security/order_security.xml',
        'security/ir.model.access.csv',
        'views/order_views.xml',
        'views/order_menu.xml',
        'views/order_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/demo.xml',],
}