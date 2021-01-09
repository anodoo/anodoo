# -*- coding: utf-8 -*-
{
    'name': "邮件营销",

    'summary': """
        邮件营销
    """,

    'description': """
        邮件营销
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-mass-mailing",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'mass_mailing'
    ],

    'data': [
        'security/mass_mailing_security.xml',
        'security/ir.model.access.csv',

        'data/mass_mailing_data.xml',

        'views/mass_mailing_views.xml',
        'views/mass_mailing_analysis_views.xml',
        'views/mass_mailing_menu.xml',
        'views/mass_mailing_templates.xml',
    ],

    'demo': [
        'demo/mass_mailing_demo.xml',
    ],
}