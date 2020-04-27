# -*- coding: utf-8 -*-
{
    'name': "Anodoo CEH",

    'summary': """
        Customer Engage Hub, 客户交互中心, 实现全渠道客户交互应用
    """,

    'description': """
        全渠道客户交互应用
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-engage",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['crm', 'calendar', 'mail', 'sale', 'sales_team',
                'anodoo_base'],

    # always loaded
    'data': [
        'data/engage_data.xml',
        #'demo/demo.xml',#demo
        'security/engage_security.xml',
        'security/ir.model.access.csv',
        'views/engage_views.xml',
        'views/engage_menu.xml',
        'views/engage_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/demo.xml',],
}