# -*- coding: utf-8 -*-
{
    'name': "客户交互",

    'summary': """
        全渠道客户交互应用
    """,

    'description': """
        全渠道客户交互应用
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-engage",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base'],

    # always loaded
    'data': [
        'data/engage_data.xml',
        'security/engage_security.xml',
        'security/ir.model.access.csv',
        'views/engage_views.xml',
        'views/engage_menu.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}