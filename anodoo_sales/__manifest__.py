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
    'website': "http://www.anodoo.com/module/anodoo-sales",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'sale', #sale的res.config.setting功能
    ],

    # always loaded
    'data': [
        'data/sales_data.xml',
        #'demo/demo.xml',#demo
        'security/sales_security.xml',
        'security/ir.model.access.csv',
        'views/sales_views.xml',
        'views/sales_menu.xml',
        'views/sales_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}