# -*- coding: utf-8 -*-
{
    'name': "客户360",

    'summary': """
        全方位的客户管理应用
    """,

    'description': """
        全方位的客户管理应用
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-cust",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,
    'auto_install': True,

    # any module necessary for this one to work correctly
    'depends': [
        'mail',
        'anodoo_crm', 'anodoo_contact'],

    # always loaded
    'data': [
        'data/cust_data.xml',
        #'demo/demo.xml',#demo
        'security/cust_security.xml',
        'security/ir.model.access.csv',
        
        'views/cust_views.xml',        
        'views/res_config_settings_views.xml',
        'views/cust_menu.xml',
        'views/cust_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/demo.xml',],
}