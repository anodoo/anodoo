# -*- coding: utf-8 -*-
{
    'name': "工时",

    'summary': """
        工时管理
    """,

    'description': """
        工时管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-timesheet",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'hr_timesheet'
    ],

    # always loaded
    'data': [
        'data/timesheet_data.xml',
        'security/timesheet_security.xml',
        'security/ir.model.access.csv',
        'views/timesheet_views.xml',
        'views/timesheet_menu.xml',
        'views/timesheet_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/timesheet_demo.xml',
    ],
}