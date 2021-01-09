# -*- coding: utf-8 -*-
{
    'name': "分析会计",

    'summary': """
        分析会计，是成本计算，项目工时等的基础模块
    """,

    'description': """
        分析会计，是成本计算，项目工时等的基础模块
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-analytic",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'analytic'
    ],

    # always loaded
    'data': [
        'data/analytic_data.xml',
        'security/analytic_security.xml',
        'security/ir.model.access.csv',
        'views/analytic_views.xml',
        'views/analytic_menu.xml',
        'views/analytic_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/analytic_demo.xml',
    ],
}