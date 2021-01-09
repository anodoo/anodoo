# -*- coding: utf-8 -*-
{
    'name': "在线学习",

    'summary': """
        在线学习
    """,

    'description': """
        在线学习
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-elearning",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'website_slides',
        'website_slides_survey',
        'website_sale_slides',
     ],

    # always loaded
    'data': [
        'data/elearning_data.xml',

        'security/elearning_security.xml',
        'security/ir.model.access.csv',  
        'views/slide_channel_views.xml',    
        'views/slide_question_views.xml',  
        'views/slide_slide_views.xml',
        'views/website_slides_templates_homepage.xml',
        'views/elearning_views.xml',
        'views/elearning_menu.xml',
        'views/elearning_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}