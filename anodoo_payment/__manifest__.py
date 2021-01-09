# -*- coding: utf-8 -*-
{
    'name': "支付",

    'summary': """
        支付管理
    """,

    'description': """
        支付管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-pay",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,


    # any module necessary for this one to work correctly
    'depends': [
        'payment',
    ],

    # always loaded
    'data': [
        'data/payment_data.xml',
        #'demo/demo.xml',#demo
        'security/payment_security.xml',
        'security/ir.model.access.csv',
        'views/payment_views.xml',
        'views/res_config_settings_views.xml',
        'views/payment_menu.xml',
        'views/payment_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}