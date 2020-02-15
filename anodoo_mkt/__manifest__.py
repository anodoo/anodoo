# -*- coding: utf-8 -*-
{
    'name': "市场营销",

    'summary': """
        市场营销
    """,

    'description': """
        市场营销
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-mkt",

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
        'data/mkt_data.xml',
        'security/mkt_security.xml',
        'security/ir.model.access.csv',
        'views/mkt_views.xml',
        'views/mkt_menu.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}