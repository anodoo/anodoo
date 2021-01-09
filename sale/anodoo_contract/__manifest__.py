# -*- coding: utf-8 -*-
{
    'name': "contract",

    'summary': """
        contract
    """,

    'description': """
        contract
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-contract",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/contract_security.xml',
        'security/ir.model.access.csv',

        'data/contract_data.xml',

        'views/contract_views.xml',
        'views/contract_analysis_views.xml',
        'views/contract_menu.xml',
        'views/contract_templates.xml',
    ],

    'demo': [
        'demo/contract_demo.xml',
    ],
}