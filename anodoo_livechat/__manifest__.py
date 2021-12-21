# -*- coding: utf-8 -*-
{
    'name': "在线客服",

    'summary': """
        在线客服，智能客服
    """,

    'description': """
        在线客服，智能客服
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-livechat",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'im_livechat'
    ],

    # always loaded
    'data': [
        'data/livechat_data.xml',
        'security/livechat_security.xml',
        'security/ir.model.access.csv',
        'views/livechat_views.xml',
        'views/livechat_menu.xml',
        'views/livechat_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/livechat_demo.xml',
    ],
}