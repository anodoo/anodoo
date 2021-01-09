# -*- coding: utf-8 -*-
{
    'name': "员工报销",

    'summary': """
        员工报销
    """,

    'description': """
        员工报销
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-hr-expense",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'hr_expense',
    ],

    'data': [
        'security/hr_expense_security.xml',
        'security/ir.model.access.csv',

        'data/hr_expense_data.xml',

        'views/hr_expense_views.xml',
        'views/hr_expense_analysis_views.xml',
        'views/hr_expense_menu.xml',
        'views/hr_expense_templates.xml',
    ],

    'demo': [
        'demo/hr_expense_demo.xml',
    ],
}