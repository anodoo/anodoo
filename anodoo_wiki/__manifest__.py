# -*- coding: utf-8 -*-
{
    'name': "Wiki百科",

    'summary': """
        wiki百科，交互渠道之一
    """,

    'description': """
        wiki百科，交互渠道之一
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-wiki",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base'
    ],

    'data': [
        'security/wiki_security.xml',
        'security/ir.model.access.csv',

        'data/wiki_data.xml',

        'views/wiki_views.xml',
        'views/wiki_analysis_views.xml',
        'views/wiki_menu.xml',
        'views/wiki_templates.xml',
    ],

    'demo': [
        'demo/wiki_demo.xml',
    ],
}