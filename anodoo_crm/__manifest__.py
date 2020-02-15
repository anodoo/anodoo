# -*- coding: utf-8 -*-
{
    'name': "客户关系管理",

    'summary': """
        客户关系管理
    """,

    'description': """
        客户关系管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/product/anodoo-crm",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base', 'anodoo_contact', 'anodoo_cust'],

    # always loaded
    'data': [
        'data/crm_data.xml',
        'security/crm_security.xml',
        'security/ir.model.access.csv',
        'views/crm_views.xml',
        'views/crm_menu.xml',
        'views/crm_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/crm_demo.xml',
    ],
}