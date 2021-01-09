# -*- coding: utf-8 -*-
{
    'name': "网站访问者",

    'summary': """
        网站访问者
    """,

    'description': """
        网站访问者
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-website",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'website'
    ],

    'data': [
        'security/website_visitor_security.xml',
        'security/ir.model.access.csv',

        'data/website_visitor_data.xml',

        'views/website_visitor_views.xml',
        'views/website_visitor_analysis_views.xml',
        'views/website_visitor_menu.xml',
        'views/website_visitor_templates.xml',
    ],

    'demo': [
        'demo/website_visitor_demo.xml',
    ],
}