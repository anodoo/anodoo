# -*- coding: utf-8 -*-
{
    'name': "笔记与备注",

    'summary': """
        笔记与备注，协同在线编辑
    """,

    'description': """
         笔记与备注，协同在线编辑
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-note",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'note'
    ],

    'data': [
        'security/note_security.xml',
        'security/ir.model.access.csv',

        'data/note_data.xml',

        'views/note_views.xml',
        'views/note_analysis_views.xml',
        'views/note_menu.xml',
        'views/note_templates.xml',
    ],

    'demo': [
        'demo/note_demo.xml',
    ],
}