# -*- coding: utf-8 -*-
{
    'name': "联系人360",

    'summary': """
        联系人管理
    """,

    'description': """
        联系人管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-contacts",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'contacts',
    ],

    'data': [
        'security/contacts_security.xml',
        'security/ir.model.access.csv',

        'data/contacts_data.xml',

        'views/res_partner_views.xml',
        'views/res_config_settings_views.xml',
        'views/contacts_views.xml',
        'views/contacts_analysis_views.xml',
        'views/contacts_menu.xml',
        'views/contacts_templates.xml',
    ],

    'demo': [
        'demo/contacts_demo.xml',
    ],
}