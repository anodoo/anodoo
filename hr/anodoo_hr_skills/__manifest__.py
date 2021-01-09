# -*- coding: utf-8 -*-
{
    'name': "员工能力",

    'summary': """
        员工能力
    """,

    'description': """
        员工能力
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-hr-skills",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'hr_skills',
    ],

    'data': [
        'security/hr_skills_security.xml',
        'security/ir.model.access.csv',

        'data/hr_skills_data.xml',

        'views/hr_skills_views.xml',
        'views/hr_skills_analysis_views.xml',
        'views/hr_skills_menu.xml',
        'views/hr_skills_templates.xml',
    ],

    'demo': [
        'demo/hr_skills_demo.xml',
    ],
}