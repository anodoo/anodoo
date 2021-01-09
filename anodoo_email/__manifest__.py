# -*- coding: utf-8 -*-
{
    'name': "邮件",

    'summary': """
        邮件交互
    """,

    'description': """
        邮件交互
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-email",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'mail',
        'fetchmail'
    ],

    # always loaded
    'data': [
        'data/email_data.xml',
        #'demo/demo.xml',#demo
        'security/email_security.xml',
        'security/ir.model.access.csv',
        'views/email_views.xml',
        'views/email_menu.xml',
        'views/email_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}