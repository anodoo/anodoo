# -*- coding: utf-8 -*-
{
    'name': "讨论",

    'summary': """
        讨论，消息和协作
    """,

    'description': """
        讨论，消息和协作
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-discuss",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'mail',
    ],

    # always loaded
    'data': [
        'data/discuss_data.xml',
        'security/discuss_security.xml',
        'security/ir.model.access.csv',
        'views/discuss_views.xml',
        'views/discuss_menu.xml',
        'views/discuss_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/discuss_demo.xml',
    ],
}