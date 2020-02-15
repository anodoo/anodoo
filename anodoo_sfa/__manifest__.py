# -*- coding: utf-8 -*-
{
    'name': "销售自动化",

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
    'depends': ['anodoo_base', 'anodoo_sale', 
                'anodoo_crm',
                'anodoo_lead', 
                'anodoo_oppor', 'anodoo_process', 'anodoo_quote', 
                'anodoo_order', 'anodoo_invoice', 'anodoo_pay'],

    # always loaded
    'data': [
        'data/sfa_data.xml',
        'security/sfa_security.xml',
        'security/ir.model.access.csv',
        'views/sfa_views.xml',
        'views/sfa_menu.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/sfa_demo.xml',
    ],
}