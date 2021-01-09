# -*- coding: utf-8 -*-
{
    'name': "门店销售",

    'summary': """
        门店销售，PoS收银
    """,

    'description': """
        门店销售，PoS收银
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-pos",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'point_of_sale'
    ],

    'data': [
        'security/pos_security.xml',
        'security/ir.model.access.csv',

        'data/pos_data.xml',

        'views/pos_views.xml',
        'views/pos_analysis_views.xml',
        'views/pos_menu.xml',
        'views/pos_templates.xml',
    ],

    'demo': [
        'demo/pos_demo.xml',
    ],
}