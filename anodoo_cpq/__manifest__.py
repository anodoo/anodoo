# -*- coding: utf-8 -*-
{
    'name': "cpq",

    'summary': """
        cpq
    """,

    'description': """
        cpq
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-cpq",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'sale_management', #直接依赖sale_management而非sale
    ],

    'data': [
        'security/cpq_security.xml',
        'security/ir.model.access.csv',

        'data/cpq_data.xml',

        'views/cpq_views.xml',
        'views/cpq_analysis_views.xml',

        'views/sale_order_template_views.xml',
        'views/res_config_settings_views.xml',
        'views/cpq_menu.xml',
        'views/cpq_templates.xml',
    ],

    'demo': [
        'demo/cpq_demo.xml',
    ],
}