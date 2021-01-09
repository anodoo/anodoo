# -*- coding: utf-8 -*-
{
    'name': "演示",

    'summary': """
        Anodoo 演示
    """,

    'description': """
        管理Anodoo演示数据，设置演示模块
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com/demo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '14.0.0', #publish at 2020-10-3
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': [
        'anodoo_base',
        #'anodoo_blog',
        #'anodoo_contact',
        #'anodoo_documents',
        #'anodoo_crm',
        #'anodoo_cust',
        #'anodoo_ecomm',
        #'anodoo_elearn',
        #'anodoo_email',
        #'anodoo_engage',
        #'anodoo_event',
        #'anodoo_forum',
        #'anodoo_invoice',
        #'anodoo_lead',
        #'anodoo_map',
        #'anodoo_meeting',
        #'anodoo_oppor',
        #'anodoo_order',
        #'anodoo_pay',
        #'anodoo_process',
        #'anodoo_product',
        #'anodoo_quote',
        #'anodoo_relation',
        #'anodoo_sale',
        #'anodoo_sfa',
        #'anodoo_sms',
        #'anodoo_team',
        #'anodoo_website',
        ],

    # always loaded
    'data': [
        #'data/demo_data.xml',
        
        'demo/base_demo.xml',
        #'demo/blog_demo.xml',
        #'demo/contact_demo.xml',
        #'demo/content_demo.xml',
        #'demo/crm_demo.xml',
        #'demo/cust_demo.xml',
        #'demo/ecomm_demo.xml',
        #'demo/elearn_demo.xml',
        #'demo/email_demo.xml',
        #'demo/engage_demo.xml',
        #'demo/event_demo.xml',
        #'demo/forum_demo.xml',
        #'demo/invoice_demo.xml',
        #'demo/lead_demo.xml',
        #'demo/map_demo.xml',
        #'demo/meeting_demo.xml',
        #'demo/oppor_demo.xml',
        #'demo/order_demo.xml',
        #'demo/pay_demo.xml',
        #'demo/portal_demo.xml',
        #'demo/process_demo.xml',
        #'demo/prod_demo.xml',
        #'demo/profile_demo.xml',
        #'demo/quote_demo.xml',
        #'demo/relation_demo.xml',
        #'demo/sale_demo.xml',
        #'demo/sfa_demo.xml',
        #'demo/sms_demo.xml',
        #'demo/team_demo.xml',
        #'demo/website_demo.xml',
        
        'security/demo_security.xml',
        'security/ir.model.access.csv',
        'views/demo_views.xml',
        'views/demo_menu.xml',
        'views/demo_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}