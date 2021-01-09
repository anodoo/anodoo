# -*- coding: utf-8 -*-
{
    'name': "员工合同",

    'summary': """
        员工合同
    """,

    'description': """
        员工合同
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/module/anodoo-hr-contract",


    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': True,
    'installable': True,

    'depends': [
        'hr_contract',
    ],

    'data': [
        'security/hr_contract_security.xml',
        'security/ir.model.access.csv',

        'data/hr_contract_data.xml',

        'views/hr_contract_views.xml',
        'views/hr_contract_analysis_views.xml',
        'views/hr_contract_menu.xml',
        'views/hr_contract_templates.xml',
    ],

    'demo': [
        'demo/hr_contract_demo.xml',
    ],
}