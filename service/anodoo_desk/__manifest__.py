# -*- coding: utf-8 -*-
{
    'name': "服务台",

    'summary': """
        服务台
    """,

    'description': """
        服务台
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-desk",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly

    'depends': [
        'base_setup',#安装web_unsplash
        'mail',
        # 'utm',
        # 'rating',
        'web_tour', #??
        # 'portal',
        'resource', #关联工作表
        #'digest',
    ],

    # always loaded
    'data': [
        'data/mail_data.xml',
        'data/desk_data.xml',
        'security/desk_security.xml',
        'security/ir.model.access.csv',
        'views/mail_activity_views.xml',
        'views/desk_stage_views.xml',
        'views/desk_tag_views.xml',
        'views/desk_channel_views.xml',
        'views/desk_type_views.xml',
        'views/desk_ticket_views.xml',
        'views/desk_analysis_views.xml',
        'views/res_partner_views.xml',
        'views/res_users_views.xml',
        'views/res_config_settings_views.xml',
        'views/desk_menu.xml',
        'views/desk_templates.xml',
        'views/assets.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/desk_demo.xml',
    ],
}