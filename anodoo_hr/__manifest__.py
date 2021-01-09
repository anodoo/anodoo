# -*- coding: utf-8 -*-
{
    'name': "员工管理",

    'summary': """
        员工管理
    """,

    'description': """
        员工管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-hr",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'hr',
    ],

    'data': [
        'security/hr_security.xml',
        'security/ir.model.access.csv',

        'data/hr_data.xml',

        'views/hr_views.xml',
        'views/hr_employee_views.xml',
        'views/hr_job_views.xml',
        'views/hr_job_level_views.xml',
        'views/hr_analysis_views.xml',
        'views/hr_menu.xml',
        'views/hr_templates.xml',
    ],

    'demo': [
        'demo/hr_demo.xml',
    ],
}