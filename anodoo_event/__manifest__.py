# -*- coding: utf-8 -*-
{
    'name': "Anodoo Event",

    'summary': """
        活动交互,包括活动营销
    """,

    'description': """
        活动交互,包括活动营销
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-event",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['event', 'website_event_track',
                'anodoo_base'],

    # always loaded
    'data': [
        'data/event_data.xml',
        'security/event_security.xml',
        'security/ir.model.access.csv',
        'views/event_views.xml',
        'views/event_menu.xml',
        'views/event_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/event_demo.xml',],
}