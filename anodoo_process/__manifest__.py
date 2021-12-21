# -*- coding: utf-8 -*-
{
    'name': "销售流程",

    'summary': """
        销售流程管理
    """,

    'description': """
        销售流程管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-process",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,


    # any module necessary for this one to work correctly
    'depends': [
        'crm'
    ],

    # always loaded
    'data': [
        'data/process_data.xml',
        #'demo/demo.xml',#demo
        'security/process_security.xml',
        'security/ir.model.access.csv',

        'views/crm_lead_views.xml',
        'views/process_views.xml',
        'views/mail_activity_views.xml',
        'views/res_config_settings_views.xml',
        'views/process_menu.xml',
        'views/process_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}