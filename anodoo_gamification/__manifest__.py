# -*- coding: utf-8 -*-
{
    'name': "游戏化积分",

    'summary': """
        游戏化积分，徽章体系
    """,

    'description': """
        游戏化积分，徽章体系
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-gamification",


    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    'depends': [
        'gamification',
    ],

    'data': [
        'security/gamification_security.xml',
        'security/ir.model.access.csv',

        'data/gamification_data.xml',

        'views/gamification_views.xml',
        'views/gamification_analysis_views.xml',
        'views/gamification_menu.xml',
        'views/gamification_templates.xml',
    ],

    'demo': [
        'demo/gamification_demo.xml',
    ],
}