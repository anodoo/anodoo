# -*- coding: utf-8 -*-
{
    'name': "短信营销",

    'summary': """
        短信营销
    """,

    'description': """
        短信营销
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-mass-sms",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'mass_mailing_sms'
    ],

    'data': [
        'security/mass_sms_security.xml',
        'security/ir.model.access.csv',

        'data/mass_sms_data.xml',

        'views/mass_sms_views.xml',
        'views/mass_sms_analysis_views.xml',
        'views/mass_sms_menu.xml',
        'views/mass_sms_templates.xml',
    ],

    'demo': [
        'demo/mass_sms_demo.xml',
    ],
}