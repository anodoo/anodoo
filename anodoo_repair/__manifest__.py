# -*- coding: utf-8 -*-
{
    'name': "维修服务",

    'summary': """
        维修服务
    """,

    'description': """
        维修服务
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-repair",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'repair'
    ],

    # always loaded
    'data': [
        'data/repair_data.xml',
        'security/repair_security.xml',
        'security/ir.model.access.csv',
        'views/repair_views.xml',
        'views/repair_menu.xml',
        'views/repair_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/repair_demo.xml',
    ],
}