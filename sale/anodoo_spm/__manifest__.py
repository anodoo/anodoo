# -*- coding: utf-8 -*-
{
    'name': "spm",

    'summary': """
        spm
    """,

    'description': """
        spm
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-spm",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'base',
    ],

    'data': [
        'security/spm_security.xml',
        'security/ir.model.access.csv',

        'data/spm_data.xml',

        'views/spm_views.xml',
        'views/spm_analysis_views.xml',
        'views/spm_menu.xml',
        'views/spm_templates.xml',
    ],

    'demo': [
        'demo/spm_demo.xml',
    ],
}