# -*- coding: utf-8 -*-
{
    'name': "营销活动",

    'summary': """
        营销活动
    """,

    'description': """
        营销活动
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-campaign",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': ['utm'],

    'data': [
        'security/campaign_security.xml',
        'security/ir.model.access.csv',

        'data/campaign_data.xml',

        'views/campaign_views.xml',
        'views/campaign_analysis_views.xml',
        'views/campaign_menu.xml',
        'views/campaign_templates.xml',
    ],

    'demo': [
        'demo/campaign_demo.xml',
    ],
}