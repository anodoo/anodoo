# -*- coding: utf-8 -*-
{
    'name': "网站表单",

    'summary': """
        网站表单
    """,

    'description': """
        网站表单
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-website",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'website_form',
    ],

    'data': [
        'security/website_form_security.xml',
        'security/ir.model.access.csv',

        'data/website_form_data.xml',
        'views/assets.xml',
        'views/website_form_views.xml',
        'views/website_form_analysis_views.xml',
        'views/website_form_menu.xml',
        'views/website_form_templates.xml',
    ],

    'demo': [
        'demo/website_form_demo.xml',
    ],
}