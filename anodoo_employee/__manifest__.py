# -*- coding: utf-8 -*-
{
    'name': "Anodoo Employee",

    'summary': """
        员工管理
    """,

    'description': """
        员工管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-employee",


    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    'depends': [
        'hr'
    ],

    'data': [
        'security/employee_security.xml',
        'security/ir.model.access.csv',

        'data/employee_data.xml',

        'views/employee_views.xml',
        'views/employee_analysis_views.xml',
        'views/employee_menu.xml',
        'views/employee_templates.xml',
    ],

    'demo': [
        'demo/employee_demo.xml',
    ],
}