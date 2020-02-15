# -*- coding: utf-8 -*-
{
    'name': "Anodoo 基础",

    'summary': """
        这个是Anodoo的所有应用和模块的基础。
    """,

    'description': """
        Anodoo需要的所有基础功能，对Odoo的所有依赖，对Odoo框架方面的修改都会在此模块中定义。
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Anodoo',
    'version': '13.1',
    'application': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['account', 'base', 'calendar', 'contacts', 'crm', 'crm_iap_lead', 
                'crm_iap_lead_website', 'delivery', 'event', 'fetchmail', 'hr', 
                'hr_attendance', 'hr_expense', 'hr_holidays', 'hr_recruitment', 
                'hr_timesheet', 'hr_timesheet_attendance', 'im_livechat', 
                'link_tracker', 'mail', 'mass_mailing', 'mass_mailing_sms', 
                'membership', 'phone_validation', 'portal', 'product', 
                'product_margin', 'project', 'purchase', 'sale', 'sale_coupon', 
                'sale_management', 'sale_timesheet', 'sales_team', 'sms', 'snailmail', 
                'stock', 'survey', 'uom', 'utm', 'website', 'website_blog', 
                'website_crm_partner_assign', 'website_customer', 'website_event', 
                'website_event_questions', 'website_event_track', 'website_form', 
                'website_forum', 'website_mail', 'website_mail_channel', 
                'website_membership', 'website_partner', 'website_profile', 
                'website_sale', 'website_sale_slides', 
                'website_slides', 'website_slides_survey'
                #'website_rating', 
                ],

    # always loaded
    'data': [
        'data/base_data.xml',
        'security/base_security.xml',
        'security/ir.model.access.csv',          
        'views/base_views.xml',         
        'views/base_menu.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}