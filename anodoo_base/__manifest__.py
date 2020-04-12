# -*- coding: utf-8 -*-
{
    'name': "基础",

    'summary': """
        基础模块,这个是对Odoo的架构,base, web等基础模块的扩展, 也是Anodoo的所有应用和模块的基础。
    """,

    'description': """
        Anodoo需要的所有基础功能，对Odoo的所有依赖，对Odoo框架方面的修改都会在此模块中定义。
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'base_setup', 'mail',
                'auth_signup', 'auth_oauth', 'auth_password_policy', 'auth_password_policy_signup',
                ],

    # always loaded
    'data': [
        'data/base_data.xml',
        'security/base_security.xml',
        'security/ir.model.access.csv', 
        #'views/iap_assets.xml',  #iap widget js依赖
        'views/ir_module_views.xml',   
        'views/res_users_views.xml', 
        'views/ir_ui_menu_views.xml',
        'views/res_company_views.xml',
        
        'views/ir_translation_views.xml',
        'views/res_country_views.xml',         
        'views/auth_oauth_views.xml',
        'views/base_views.xml',                 
        'views/base_menu.xml',
        'views/base_templates.xml',        
        'views/res_config_settings_views.xml', 
    ],
    # only loaded in demonstration mode
    'demo': ['demo/base_demo.xml',],
}