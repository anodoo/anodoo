# -*- coding: utf-8 -*-
{
    'name': "qrcode",

    'summary': """
        qrcode
    """,

    'description': """
        qrcode
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-qrcode",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/qrcode_security.xml',
        'security/ir.model.access.csv',

        'data/qrcode_data.xml',

        'views/qrcode_views.xml',
        'views/qrcode_analysis_views.xml',
        'views/qrcode_menu.xml',
        'views/qrcode_templates.xml',
    ],

    'demo': [
        'demo/qrcode_demo.xml',
    ],
}