# -*- coding: utf-8 -*-
{
    'name': "营销线索",

    'summary': """
        营销线索
    """,

    'description': """
        营销线索
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-lead",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,
    'auto_install': True,

    # any module necessary for this one to work correctly
    'depends': ['crm', 'iap', 'crm_iap_lead', 'crm_iap_lead_enrich', #'crm_iap_lead_website',
                'anodoo_mktauto'],

    # always loaded
    'data': [
        'security/lead_security.xml',
        'security/ir.model.access.csv',
        'wizard/crm_lead_lost_views.xml',
        'wizard/crm_merge_opportunities_views.xml',
        'wizard/crm_lead_to_opportunity_views.xml',
        'views/lead_views.xml',
        'views/lead_menu.xml',
        'views/lead_templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': ['demo/lead_demo.xml',],
}