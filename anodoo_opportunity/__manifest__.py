# -*- coding: utf-8 -*-
{
    'name': "商机管理",

    'summary': """
        商机管理
    """,

    'description': """
        商机管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-opportunity",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,


    # any module necessary for this one to work correctly
    'depends': [
        'crm',
    ],

    # always loaded
    'data': [
        'data/opportunity_data.xml',
        #'demo/demo.xml',#demo
        'security/opportunity_security.xml',
        'security/ir.model.access.csv',

        'views/opportunity_stage_views.xml',
        'wizard/crm_opportunity_lost_views.xml',
        'views/crm_lead_views.xml',
        'views/opportunity_views.xml',
        'views/res_config_settings_views.xml',
        'views/opportunity_menu.xml',
        'views/opportunity_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}