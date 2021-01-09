# -*- coding: utf-8 -*-
{
    'name': "social_media",

    'summary': """
        social_media
    """,

    'description': """
        social_media
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-social",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'social_media',
        'website'
    ],

    'data': [
        'security/social_media_security.xml',
        'security/ir.model.access.csv',

        'data/social_media_data.xml',

        'views/res_company_views.xml',
        'views/res_config_settings_views.xml',
        'views/social_media_views.xml',
        'views/social_media_analysis_views.xml',
        'views/social_media_menu.xml',
        'views/social_media_templates.xml',
    ],

    'demo': [
        'demo/social_media_demo.xml',
    ],
}