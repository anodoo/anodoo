# -*- coding: utf-8 -*-
{
    'name': "Anodoo 演示",

    'summary': """
        Anodoo的所有功能演示
    """,

    'description': """
        Anodoo的所有功能演示
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base', 'anodoo_cust', 'anodoo_engage', 'anodoo_engage_email',
                'anodoo_engage_event', 'anodoo_engage_meeting', 'anodoo_engage_sms',
                'anodoo_engage_website', 'anodoo_lead', 'anodoo_mkt', 'anodoo_mktauto',
                'anodoo_prod', 'anodoo_proj', 'anodoo_sale', 'anodoo_sfa', 'anodoo_team'],

    # always loaded
    'data': [
        'data/demo_data.xml',
        'security/demo_security.xml',
        'security/ir.model.access.csv',
        'views/demo_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
