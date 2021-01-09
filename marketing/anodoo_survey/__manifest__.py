# -*- coding: utf-8 -*-
{
    'name': "survey",

    'summary': """
        survey
    """,

    'description': """
        survey
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-survey",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/survey_security.xml',
        'security/ir.model.access.csv',

        'data/survey_data.xml',

        'views/survey_views.xml',
        'views/survey_analysis_views.xml',
        'views/survey_menu.xml',
        'views/survey_templates.xml',
    ],

    'demo': [
        'demo/survey_demo.xml',
    ],
}