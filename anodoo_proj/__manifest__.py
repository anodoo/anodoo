# -*- coding: utf-8 -*-
{
    'name': "Anodoo Project",

    'summary': """
        项目管理
    """,

    'description': """
        项目管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-proj",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['project',
                'anodoo_base'],

    # always loaded
    'data': [
        'data/proj_data.xml',
        #'demo/demo.xml',#demo
        'security/proj_security.xml',
        'security/ir.model.access.csv',
        'views/proj_views.xml',
        'views/res_config_settings_views.xml',
        'views/proj_menu.xml',
        'views/proj_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/demo.xml',],
}