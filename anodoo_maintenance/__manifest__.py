# -*- coding: utf-8 -*-
{
    'name': "质保服务",

    'summary': """
        质保服务，维护，保养服务
    """,

    'description': """
        质保服务，维护，保养服务
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-maintenance",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'maintenance'
    ],

    # always loaded
    'data': [
        'data/maintenance_data.xml',
        'security/maintenance_security.xml',
        'security/ir.model.access.csv',
        'views/maintenance_views.xml',
        'views/maintenance_menu.xml',
        'views/maintenance_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/maintenance_demo.xml',
    ],
}