# -*- coding: utf-8 -*-
{
    'name': "日历",

    'summary': """
        日历
    """,

    'description': """
        日历，会议安排，预约
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-calendar",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'calendar'
    ],

    'data': [
        'security/calendar_security.xml',
        'security/ir.model.access.csv',

        'data/calendar_data.xml',

        'views/calendar_views.xml',
        'views/calendar_analysis_views.xml',
        'views/calendar_menu.xml',
        'views/calendar_templates.xml',
    ],

    'demo': [
        'demo/calendar_demo.xml',
    ],
}