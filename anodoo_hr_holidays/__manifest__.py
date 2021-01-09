# -*- coding: utf-8 -*-
{
    'name': "员工假期",

    'summary': """
        员工假期
    """,

    'description': """
        员工假期
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-hr-holidays",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'hr_holidays',
    ],

    'data': [
        'security/hr_holidays_security.xml',
        'security/ir.model.access.csv',

        'data/hr_holidays_data.xml',

        'views/hr_holidays_views.xml',
        'views/hr_holidays_analysis_views.xml',
        'views/hr_holidays_menu.xml',
        'views/hr_holidays_templates.xml',
    ],

    'demo': [
        'demo/hr_holidays_demo.xml',
    ],
}