# -*- coding: utf-8 -*-
{
    'name': "联系人",

    'summary': """
        联系人管理
    """,

    'description': """
        联系人管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-contact",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base', 'anodoo_cust'],

    # always loaded
    'data': [
        'data/contact_data.xml',
        'security/contact_security.xml',
        'security/ir.model.access.csv',
        'views/contact_views.xml',
        'views/contact_menu.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}