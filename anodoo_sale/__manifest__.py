# -*- coding: utf-8 -*-
{
    'name': "anodoo_sale",

    'summary': """
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base', 'crm', 'sale', 'website_crm_partner_assign'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_menu_action.xml',
        'views/sale_menu.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}