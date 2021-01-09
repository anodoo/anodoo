# -*- coding: utf-8 -*-
{
    'name': "asset",

    'summary': """
        asset
    """,

    'description': """
        asset
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-asset",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/asset_security.xml',
        'security/ir.model.access.csv',

        'data/asset_data.xml',

        'views/asset_views.xml',
        'views/asset_analysis_views.xml',
        'views/asset_menu.xml',
        'views/asset_templates.xml',
    ],

    'demo': [
        'demo/asset_demo.xml',
    ],
}