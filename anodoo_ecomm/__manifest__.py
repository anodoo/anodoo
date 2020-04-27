# -*- coding: utf-8 -*-
{
    'name': "Anodoo Commerce",

    'summary': """
        电子商务
    """,

    'description': """
        电子商务
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-ecomm",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['sales_team', 'product', 'sale_coupon', 'payment', 'delivery', 'website_sale', 'website_sale_comparison', 'website_sale_stock',
                'anodoo_website', 'anodoo_sfa'],

    # always loaded
    'data': [
        'data/ecomm_data.xml',
        #'demo/demo.xml',#demo
        'security/ecomm_security.xml',
        'security/ir.model.access.csv',
        'views/ecomm_views.xml',
        'views/product_views.xml',
        'views/res_config_settings_views.xml',
        'views/ecomm_menu.xml',
        'views/ecomm_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/demo.xml',],
}