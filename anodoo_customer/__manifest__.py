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
    'website': "http://www.anodoo.com/module/anodoo-customer",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        # 'contacts',
        'account', #odoo中，通过customer_rank标识客户，因此，需依赖account
    ],

    'data': [
        'security/customer_security.xml',
        'security/ir.model.access.csv',

        'data/customer_data.xml',

        'views/res_partner_views.xml',
        'views/customer_views.xml',
        'views/customer_analysis_views.xml',
        'views/res_config_settings_views.xml',
        'views/customer_menu.xml',
        'views/customer_templates.xml',
    ],

    'demo': [
        'demo/customer_demo.xml',
    ],
}