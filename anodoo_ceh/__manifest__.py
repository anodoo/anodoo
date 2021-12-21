# -*- coding: utf-8 -*-
{
    'name': "交互中心管理",

    'summary': """
        Customer Engage Hub, 客户交互中心, 实现全渠道客户交互应用
    """,

    'description': """
        全渠道客户交互应用
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-ceh",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'mail'
    ],

    # always loaded
    'data': [
        'data/ceh_data.xml',
        #'demo/demo.xml',#demo
        'security/ceh_security.xml',
        'security/ir.model.access.csv',
        'views/ceh_views.xml',
        'views/ceh_menu.xml',
        'views/ceh_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}