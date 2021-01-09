# -*- coding: utf-8 -*-
{
    'name': "客户关系管理",

    'summary': """
        客户关系管理，CRM
    """,

    'description': """
        客户关系管理，CRM
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-crm",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'crm',
    ],

    'data': [
        'security/crm_security.xml',
        'security/ir.model.access.csv',

        'data/crm_data.xml',

        'views/crm_views.xml',
        'views/crm_analysis_views.xml',
        'views/crm_menu.xml',
        'views/crm_templates.xml',
    ],

    'demo': [
        'demo/crm_demo.xml',
    ],
}