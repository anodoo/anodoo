# -*- coding: utf-8 -*-
{
    'name': "客户关系",

    'summary': """
        客户相关关系的管理,包括客户关系,联系人关系,用户关系,以及组织关系等.
    """,

    'description': """
        客户相关关系的管理,包括客户关系,联系人关系,用户关系,以及组织关系等.
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-relationship",


    'category': 'Anodoo',
    'version': '13.1',
    'application': True,
    'installable': True,

    'depends': [
        'anodoo_contacts', #关系是针对客户，联系人，因此依赖这两个模块
        'anodoo_customer', #关系是针对客户，联系人，因此依赖这两个模块
    ],

    'data': [
        'security/relationship_security.xml',
        'security/ir.model.access.csv',

        'data/relationship_data.xml',

        'views/res_partner_views.xml',
        'views/res_config_settings_views.xml',
        'views/relationship_views.xml',
        'views/relationship_analysis_views.xml',
        'views/relationship_menu.xml',
        'views/relationship_templates.xml',
    ],

    'demo': [
        'demo/relationship_demo.xml',
    ],
}