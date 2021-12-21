# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import datetime, timedelta
from odoo import fields, models, api
from odoo.http import request


class WebsiteTrack(models.Model):
    _inherit = 'website.track'

    referrer = fields.Text('Referrer信息')


class WebsiteVisitor(models.Model):
    _inherit = 'website.visitor'

    #Override, 增加referrer
    def _handle_website_page_visit(self, website_page, visitor_sudo):
        """ Called on dispatch. This will create a website.visitor if the http request object
        is a tracked website page or a tracked view. Only on tracked elements to avoid having
        too much operations done on every page or other http requests.
        Note: The side effect is that the last_connection_datetime is updated ONLY on tracked elements."""
        url = request.httprequest.url
        
        #增加referrer
        referrer_url = request.httprequest.headers.get('Referer', '')
        
        website_track_values = {
            'url': url,
            'visit_datetime': datetime.now(),
            'referrer': referrer_url
        }
        if website_page:
            website_track_values['page_id'] = website_page.id
            domain = [('page_id', '=', website_page.id)]
        else:
            domain = [('url', '=', url)]
        visitor_sudo._add_tracking(domain, website_track_values)
        if visitor_sudo.lang_id.id != request.lang.id:
            visitor_sudo.write({'lang_id': request.lang.id})

