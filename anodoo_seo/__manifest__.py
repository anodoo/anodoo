# -*- coding: utf-8 -*-
{
    'name': "seo",

    'summary': """
        seo
    """,

    'description': """
        seo
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-seo",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'website', #基于website，因为/robots.txt，/sitemap.xml等都是在website模块

    ],

    'data': [
        'security/seo_security.xml',
        'security/ir.model.access.csv',

        'data/seo_data.xml',

        'views/res_config_settings_views.xml',
        'views/seo_views.xml',
        'views/seo_analysis_views.xml',
        'views/seo_menu.xml',
        'views/seo_templates.xml',
    ],

    'demo': [
        'demo/seo_demo.xml',
    ],
}