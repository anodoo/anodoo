# -*- coding: utf-8 -*-
{
    'name': "Anodoo Team",

    'summary': """
        团队协同
    """,

    'description': """
        团队协同
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-team",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,
    'auto_install': True,

    # any module necessary for this one to work correctly
    'depends': ['mail', 'sales_team', 'note_pad',
                'anodoo_base'],

    # always loaded
    'data': [
        'data/team_data.xml',
        #'demo/demo.xml',#demo
        'security/team_security.xml',
        'security/ir.model.access.csv',
        'views/team_views.xml',
        'views/note_views.xml',
        'views/res_config_settings_views.xml',
        'views/team_menu.xml',
        'views/team_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/demo.xml',],
}