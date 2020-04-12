# -*- coding: utf-8 -*-
{
    'name': "客户关系",

    'summary': """
        客户相关关系的管理,包括客户关系,联系人关系,用户关系,以及组织关系等.
    """,

    'description': """
        客户相关关系的管理,包括客户关系,联系人关系,用户关系,以及组织关系等.
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-relation",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,
    'auto_install': True,

    # any module necessary for this one to work correctly
    'depends': ['anodoo_crm'],

    # always loaded
    'data': [
        'data/relation_data.xml',
        'security/relation_security.xml',
        'security/ir.model.access.csv',
        'views/relation_views.xml',
        'views/relation_menu.xml',
        'views/relation_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/relation_demo.xml',],
}