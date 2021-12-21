# -*- coding: utf-8 -*-
{
    'name': "团队",

    'summary': """
        团队，基础模块
    """,

    'description': """
        团队，基础模块
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-team",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True, #虚拟类，虚拟模块，不安装


    # any module necessary for this one to work correctly
    'depends': [
        'mail',
    ],

    # always loaded
    'data': [
        'data/team_data.xml',
        'security/team_security.xml',
        'security/ir.model.access.csv',
        'views/team_views.xml',
        'views/team_template_views.xml',
        'views/team_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': ['demo/team_demo.xml'],
}