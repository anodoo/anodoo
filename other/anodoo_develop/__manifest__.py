# -*- coding: utf-8 -*-
{
    'name': "开发工具",

    'summary': """
        开发工具
        """,

    'description': """
        开发工具
    """,

    'author': "anodoo",
    'website': "http://www.anodoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/develop_menu.xml',
        'views/develop_views.xml',
        'views/develop_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/develop_demo.xml',
    ],
}
