# -*- coding: utf-8 -*-
{
    'name': "Anodoo Content",

    'summary': """
        内容管理,包括文档管理,各种内容库管理,以及对营销内容,销售内容,服务内容的支持
    """,

    'description': """
        内容管理,包括文档管理,各种内容库管理,以及对营销内容,销售内容,服务内容的支持
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-content",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base'],

    # always loaded
    'data': [
        'data/content_data.xml',
        'security/content_security.xml',
        'security/ir.model.access.csv',
        'views/content_views.xml',
        'views/res_config_settings_views.xml',
        'views/content_menu.xml',
        'views/content_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/content_demo.xml',],
}