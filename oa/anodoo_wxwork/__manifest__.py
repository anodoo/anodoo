# -*- coding: utf-8 -*-
{
    'name': "wxwork",

    'summary': """
        wxwork
    """,

    'description': """
        wxwork
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-wxwork",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/wxwork_security.xml',
        'security/ir.model.access.csv',

        'data/wxwork_data.xml',

        'views/wxwork_views.xml',
        'views/wxwork_analysis_views.xml',
        'views/wxwork_menu.xml',
        'views/wxwork_templates.xml',
    ],

    'demo': [
        'demo/wxwork_demo.xml',
    ],
}