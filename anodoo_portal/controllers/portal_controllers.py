# -*- coding: utf-8 -*-

from odoo import http

from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request, route
import werkzeug

class AnodooPortal(CustomerPortal):

    @route(['/portal',
            '/portal/<string:portal>',
            ], type='http', auth="user", website=True)
    def portal_home(self, portal=None, **kw):
        current_portal = None
        if portal:
            p = request.env['anodoo.portal']
            portals = p.search([('code', '=', portal)], limit=1)
            if len(portals) > 0:
                current_portal = portals[0]

        if not portal or not current_portal:
            return werkzeug.utils.redirect('/my', code=302)

        # todo:权限判断
        #         group_id = current_portal.group_id
        #         if not request.env.user.has_group(group_id):
        #             raise AccessError(_("Access Denied"))

        view = current_portal.view_id.xml_id

        values = self._prepare_portal_layout_values()
        return request.render(view, values)