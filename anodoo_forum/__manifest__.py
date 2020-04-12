# -*- coding: utf-8 -*-
{
    'name': "Anodoo Forum",

    'summary': """
        论坛
    """,

    'description': """
        论坛
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-forum",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['website_forum',
                'anodoo_profile'],

    # always loaded
    'data': [
        'data/forum_data.xml',
        'security/forum_security.xml',
        'security/ir.model.access.csv',
        'views/forum_views.xml',
        'views/forum.xml',
        'views/res_config_settings_views.xml',
        'views/forum_menu.xml',
        'views/forum_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/forum_demo.xml',],
}