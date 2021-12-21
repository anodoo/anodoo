# -*- coding: utf-8 -*-
{
    'name': "短信",

    'summary': """
        短信交互
    """,

    'description': """
        短信交互
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-sms",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'sms'
    ],

    # always loaded
    'data': [
        'data/sms_data.xml',
        #'demo/demo.xml',#demo
        'security/sms_security.xml',
        'security/ir.model.access.csv',
        'views/sms_views.xml',
        'views/sms_menu.xml',
        'views/sms_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}