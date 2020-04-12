# -*- coding: utf-8 -*-
{
    'name': "Anodoo Metting",

    'summary': """
        会议交互,通过线上,线下会议等形式和客户交互
    """,

    'description': """
        会议交互,通过线上,线下会议等形式和客户交互
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-meeting",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['calendar',
                'anodoo_base'],

    # always loaded
    'data': [
        'data/meeting_data.xml',
        'security/meeting_security.xml',
        'security/ir.model.access.csv',
        'views/meeting_views.xml',
        'views/meeting_menu.xml',
        'views/meeting_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/meeting_demo.xml',],
}