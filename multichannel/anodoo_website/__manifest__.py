# -*- coding: utf-8 -*-
{
    'name': "网站",

    'summary': """
        网站,CMS系统
    """,

    'description': """
        网站,CMS系统
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-website",


    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    'depends': [
        'website'
    ],

    'data': [
        'security/website_security.xml',
        'security/ir.model.access.csv',

        'data/website_data.xml',

        'views/website_views.xml',
        'views/website_analysis_views.xml',
        'views/website_menu.xml',
        'views/website_templates.xml',
    ],

    'demo': [
        'demo/website_demo.xml',
    ],
}