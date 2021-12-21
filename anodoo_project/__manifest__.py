# -*- coding: utf-8 -*-
{
    'name': "项目管理",

    'summary': """
        项目管理
    """,

    'description': """
        项目管理
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-project",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'project',
    ],

    # always loaded
    'data': [
        'data/project_data.xml',
        #'demo/demo.xml',#demo
        'security/project_security.xml',
        'security/ir.model.access.csv',
        'views/project_views.xml',
        'views/project_stage_views.xml',
        'views/project_type_views.xml',
        'views/project_menu.xml',
        'views/project_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}