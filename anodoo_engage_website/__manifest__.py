# -*- coding: utf-8 -*-
{
    'name': "anodoo_engage_website",

    'summary': """
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Anodoo",
    'website': "http://www.anodoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base', 'website', 'website_form', 'website_mail', 'website_mail_channel',
                'website_rating', 'survey', 'website_blog', 'website_slides', 'website_slides_survey', 'website_forum', 
                'website_event', 'website_event_track', 'portal', 'website_membership', 'website_profile', 
                'website_customer', 'website_partner', 'website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/engage_website_menu_action.xml',
        'views/engage_website_menu.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}