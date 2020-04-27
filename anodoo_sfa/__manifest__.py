# -*- coding: utf-8 -*-
{
    'name': "Anodoo SFA",

    'summary': """
        销售自动化
    """,

    'description': """
        销售自动化
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/product/anodoo-sfa",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'anodoo_team', 'anodoo_proj', 'anodoo_content', 'anodoo_prod', 'anodoo_crm', ],

    # always loaded
    'data': [
        'data/sfa_data.xml',
        #'demo/demo.xml',#demo
        'security/sfa_security.xml',
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'views/sfa_views.xml',
        'views/sfa_menu.xml',
        'views/sfa_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/demo.xml',],
}