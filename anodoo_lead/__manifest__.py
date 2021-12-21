# -*- coding: utf-8 -*-
{
    'name': "线索",

    'summary': """
        销售线索
    """,

    'description': """
        销售线索
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-lead",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'crm',
        'crm_iap_lead', 'crm_iap_lead_website',#这两个模块主要是第三方lead挖掘使用的，临时性的
    ],

    # always loaded
    'data': [
        'data/lead_data.xml',
        #'demo/demo.xml',#demo
        'security/lead_security.xml',
        'security/ir.model.access.csv',


        'views/lead_stage_views.xml',
        'wizard/crm_lead_lost_views.xml',
        'views/crm_lead_views.xml',
        'views/lead_qualify_views.xml',
        'wizard/crm_merge_opportunities_views.xml',
        'wizard/crm_lead_to_opportunity_views.xml',
        'views/lead_views.xml',
        'views/res_config_settings_views.xml',
        'views/lead_menu.xml',
        'views/lead_templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': ['demo/lead_demo.xml'],
}