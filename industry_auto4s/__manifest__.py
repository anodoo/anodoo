# -*- coding: utf-8 -*-
{
    'name': "汽车4S店",

    'summary': """
        汽车4S店，行业版本
    """,

    'description': """
        汽车4S店，行业版本
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-auto4s",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'anodoo_demo'
    ],

    # always loaded
    'data': [
        'data/auto4s_data.xml',
        'security/auto4s_security.xml',
        'security/ir.model.access.csv',
        'views/auto4s_views.xml',
        'views/auto4s_menu.xml',
        'views/auto4s_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/auto4s_demo.xml',
    ],
}