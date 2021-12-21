# -*- coding: utf-8 -*-
{
    'name': "销售预测",

    'summary': """
        销售目标，计划与预测
    """,

    'description': """
        销售目标，计划与预测
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-forecast",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'anodoo_territory',#依赖了销售区域的概念，后续通过粘合模块实现
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