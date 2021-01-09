# -*- coding: utf-8 -*-
{
    'name': "mrp",

    'summary': """
        mrp
    """,

    'description': """
        mrp
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-mrp",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/mrp_security.xml',
        'security/ir.model.access.csv',

        'data/mrp_data.xml',

        'views/mrp_views.xml',
        'views/mrp_analysis_views.xml',
        'views/mrp_menu.xml',
        'views/mrp_templates.xml',
    ],

    'demo': [
        'demo/mrp_demo.xml',
    ],
}