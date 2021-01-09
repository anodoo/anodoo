# -*- coding: utf-8 -*-
{
    'name': "员工考勤",

    'summary': """
        员工考勤
    """,

    'description': """
        员工考勤
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-hr-attendance",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'hr_attendance',
    ],

    'data': [
        'security/hr_attendance_security.xml',
        'security/ir.model.access.csv',

        'data/hr_attendance_data.xml',

        'views/hr_attendance_views.xml',
        'views/hr_attendance_analysis_views.xml',
        'views/hr_attendance_menu.xml',
        'views/hr_attendance_templates.xml',
    ],

    'demo': [
        'demo/hr_attendance_demo.xml',
    ],
}