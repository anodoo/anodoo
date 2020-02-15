# -*- coding: utf-8 -*-
{
    'name': "交互渠道-短信",

    'summary': """
        短信交互,包括短信营销
    """,

    'description': """
        短信交互,包括短信营销
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-engage-sms",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base', 'anodoo_engage', 'anodoo_mktauto'],

    # always loaded
    'data': [
        'data/engage_sms_data.xml',
        'security/engage_sms_security.xml',
        'security/ir.model.access.csv',
        'views/engage_sms_views.xml',
        'views/engage_sms_menu.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}