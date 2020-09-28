# -*- coding: utf-8 -*-
{
    'name': "Anodoo MAP",

    'summary': """
        Marketing Antomation Platfrom, 营销自动化
    """,

    'description': """
        营销自动化
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-mktauto",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'anodoo_team', 'anodoo_proj', 'anodoo_content'],

    # always loaded
    'data': [
        'data/map_data.xml',
        #'demo/demo.xml',#demo
        'security/map_security.xml',
        'security/ir.model.access.csv',
        'views/map_views.xml',        
        'views/res_config_settings_views.xml',
        'views/map_menu.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/demo.xml',],
}