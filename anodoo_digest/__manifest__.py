# -*- coding: utf-8 -*-
{
    'name': "摘要邮件",

    'summary': """
        摘要邮件
    """,

    'description': """
        摘要邮件
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-digest",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'digest'
    ],

    # always loaded
    'data': [
        'data/digest_data.xml',
        'security/digest_security.xml',
        'security/ir.model.access.csv',
        'views/digest_tip_views.xml',
        'views/digest_menu.xml',
        'views/digest_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/digest_demo.xml',
    ],
}