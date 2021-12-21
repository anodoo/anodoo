# -*- coding: utf-8 -*-
{
    'name': "员工招聘",

    'summary': """
        员工招聘
    """,

    'description': """
        员工招聘
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-hr-recruitment",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'hr_recruitment',
    ],

    'data': [
        'security/hr_recruitment_security.xml',
        'security/ir.model.access.csv',

        'data/hr_recruitment_data.xml',

        'views/hr_recruitment_views.xml',
        'views/hr_recruitment_analysis_views.xml',
        'views/hr_recruitment_menu.xml',
        'views/hr_recruitment_templates.xml',
    ],

    'demo': [
        'demo/hr_recruitment_demo.xml',
    ],
}