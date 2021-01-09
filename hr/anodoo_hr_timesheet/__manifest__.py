# -*- coding: utf-8 -*-
{
    'name': "员工工时",

    'summary': """
        员工工时
    """,

    'description': """
        员工工时
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-hr-timesheet",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'hr_timesheet',
    ],

    'data': [
        'security/hr_timesheet_security.xml',
        'security/ir.model.access.csv',

        'data/hr_timesheet_data.xml',

        'views/hr_timesheet_views.xml',
        'views/hr_timesheet_analysis_views.xml',
        'views/hr_timesheet_menu.xml',
        'views/hr_timesheet_templates.xml',
    ],

    'demo': [
        'demo/hr_timesheet_demo.xml',
    ],
}