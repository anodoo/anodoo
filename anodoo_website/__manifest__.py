# -*- coding: utf-8 -*-
{
    'name': "Anodoo Website",

    'summary': """
        官网CMS
    """,

    'description': """
        面向客户的官网
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-website",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['website', 'website_theme_install', 'website_form', 'website_livechat',
                'anodoo_portal'],

    # always loaded
    'data': [
        'data/website_data.xml',
        #'demo/demo.xml',#demo
        'security/website_security.xml',
        'security/ir.model.access.csv',
        'views/website_views.xml',
        'views/res_company_views.xml',
        'views/res_config_settings_views.xml',
        'views/website_menu.xml',
        'views/website_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/demo.xml',],
}