# -*- coding: utf-8 -*-
{
    'name': "财务管理",

    'summary': """
        财务，会计，发票等，是销售管理的基础模块
    """,

    'description': """
        财务，会计，发票等，是销售管理的基础模块
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-account",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'account',

        'l10n_cn',
    ],

    # always loaded
    'data': [
        'data/account_data.xml',
        'security/account_security.xml',
        'security/ir.model.access.csv',
        'views/account_views.xml',
        'views/account_menu.xml',
        'views/account_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/account_demo.xml',
    ],
}