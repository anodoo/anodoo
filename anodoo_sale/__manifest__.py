# -*- coding: utf-8 -*-
{
    'name': "Anodoo Sale",

    'summary': """
        销售管理
    """,

    'description': """
        销售管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-sale",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['sale', 'sales_team',
                'anodoo_team', 'anodoo_proj', 'anodoo_content', 'anodoo_sfa'],

    # always loaded
    'data': [
        'data/sale_data.xml',
        'security/sale_security.xml',
        'security/ir.model.access.csv',
        'views/sale_views.xml',
        'views/sale_menu.xml',
        'views/sale_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/sale_demo.xml',],
}