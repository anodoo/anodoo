# -*- coding: utf-8 -*-
{
    'name': "网站会员信息",

    'summary': """
        网站会员信息
    """,

    'description': """
        网站会员信息
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-website",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'website_profile'
    ],

    'data': [
        'security/website_profile_security.xml',
        'security/ir.model.access.csv',

        'data/website_profile_data.xml',
        'views/res_config_settings_views.xml',
        'views/website_profile_views.xml',
        'views/website_profile_analysis_views.xml',
        'views/website_profile_menu.xml',
        'views/website_profile_templates.xml',
    ],

    'demo': [
        'demo/website_profile_demo.xml',
    ],
}