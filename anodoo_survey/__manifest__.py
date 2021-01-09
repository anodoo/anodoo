# -*- coding: utf-8 -*-
{
    'name': "问卷调查",

    'summary': """
        问卷调查，客户交互渠道之一
    """,

    'description': """
        问卷调查，客户交互渠道之一
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-survey",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'survey'
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