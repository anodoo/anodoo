# -*- coding: utf-8 -*-
{
    'name': "代理商销售",

    'summary': """
        PRM，代理商销售
    """,

    'description': """
        PRM，代理商销售，包括内网和外网
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-prm",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'website_crm_partner_assign'
    ],

    'data': [
        'security/prm_security.xml',
        'security/ir.model.access.csv',

        'data/prm_data.xml',

        'views/res_config_settings_views.xml',
        'views/res_partner_views.xml',
        'views/partner_type_views.xml',
        'views/prm_views.xml',
        'views/prm_analysis_views.xml',
        'views/prm_menu.xml',
        'views/prm_templates.xml',
    ],

    'demo': [
        'demo/prm_demo.xml',
    ],
}