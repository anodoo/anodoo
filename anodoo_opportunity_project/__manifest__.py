# -*- coding: utf-8 -*-
{
    'name': "opportunity_project",

    'summary': """
        opportunity_project
    """,

    'description': """
        opportunity_project
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-opportunity",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    'depends': [
        'project', #商机项目，未来通过独立module来实现
    ],

    'data': [
        'security/opportunity_project_security.xml',
        'security/ir.model.access.csv',

        'data/opportunity_project_data.xml',

        'views/crm_lead_views.xml',
        'views/opportunity_project_views.xml',
        'views/opportunity_project_views.xml',
        'views/opportunity_project_analysis_views.xml',
        'views/opportunity_project_menu.xml',
        'views/opportunity_project_templates.xml',
    ],

    'demo': [
        'demo/opportunity_project_demo.xml',
    ],
}