# -*- coding: utf-8 -*-
{
    'name': "fleet",

    'summary': """
        fleet
    """,

    'description': """
        fleet
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-fleet",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/fleet_security.xml',
        'security/ir.model.access.csv',

        'data/fleet_data.xml',

        'views/fleet_views.xml',
        'views/fleet_analysis_views.xml',
        'views/fleet_menu.xml',
        'views/fleet_templates.xml',
    ],

    'demo': [
        'demo/fleet_demo.xml',
    ],
}