# -*- coding: utf-8 -*-
{
    'name': "Anodoo Forecast",

    'summary': """
        销售目标，计划与预测
    """,

    'description': """
        销售目标，计划与预测
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-forecast",


    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    'depends': [
        'base'
    ],

    'data': [
        'security/forecast_security.xml',
        'security/ir.model.access.csv',

        'data/forecast_data.xml',

        'views/forecast_views.xml',
        'views/forecast_analysis_views.xml',
        'views/forecast_menu.xml',
        'views/forecast_templates.xml',
    ],

    'demo': [
        'demo/forecast_demo.xml',
    ],
}