# -*- coding: utf-8 -*-
{
    'name': "anodoo_engage_event",

    'summary': """
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base', 'anodoo_engage', 'anodoo_mktauto'],

    # always loaded
    'data': [
        'data/engage_event_data.xml',
        # 'security/ir.model.access.csv',
        'views/engage_event_menu.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}