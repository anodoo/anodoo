# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Customer(models.Model):

    _inherit = 'res.partner'

    customer_identity = fields.Char('唯一标识信息', help='客户唯一标识信息')

    # belong_team_id = fields.Many2one('crm.team', string='客户团队', help='客户所属的客户团队')
    # 团队功能后续扩展



    customer_relation_customer_ids = fields.One2many('anodoo.customer.relation.customer', 'customer_id', string='客户与客户关系')

    def _default_customer_type(self):
        customer_types = self.env['anodoo.customer.type'].search([], order="is_default desc, sequence", limit=1)
        if customer_types:
            return customer_types[0]
        return self.env['anodoo.customer.type']

    customer_type = fields.Many2one('anodoo.customer.type', string='客户类型', default=_default_customer_type,
                                    domain=[('is_active', '=', True)], help='客户类型定义，可扩展')
    # 面向开发者来修改
    # customer_type = fields.Selection([('company', '公司客户'), ('person', '个人客户'), ('family', '家庭客户'), ('government', '政府客户'), ('organization', '组织客户')],
    #                       string='客户类型', default='company', help='客户类型定义，可扩展')
    customer_type_str = fields.Char(related='customer_type.type')

    def _default_customer_size(self):
        customer_sizes = self.env['anodoo.customer.size'].search([], order="is_default desc, sequence", limit=1)
        if customer_sizes:
            return customer_sizes[0]
        return self.env['anodoo.customer.size']

    customer_size = fields.Many2one('anodoo.customer.size', string='客户规模', default=_default_customer_size,
                                    domain=[('is_active', '=', True)], help='客户规模定义，可扩展')
    # customer_size = fields.Selection([('KA', '大客户'), ('SMB', '中小客户')],
    #                        string='客户规模', default='KA', help='客户规模定义，可扩展')
    customer_size_int = fields.Integer(related='customer_size.size')

    customer_priority = fields.Selection([('0', 'Low'), ('1', 'Medium'), ('2', 'High'), ('3', 'Very High')],
                                         string='优先级', index=True, default='0')

    lifetime_id = fields.Many2one('anodoo.customer.lifetime', string='客户生命周期', help='客户使用的生命周期定义')

    lifetime_stage_id = fields.Many2one('anodoo.customer.lifetime.stage', string='客户生命周期阶段', help='客户当前的生命周期阶段',
                                        domain="[('lifetime_id','=', lifetime_id)]")

    is_prospect = fields.Boolean('是否潜在客户', compute='_compute_is_prospect', store=True)
    is_losing = fields.Boolean('是否流失客户', compute='_compute_is_losing', store=True)
    is_success = fields.Boolean('是否成功客户', compute='_compute_is_success', store=True)






    @api.model
    def default_get(self, default_fields):
        # OVERRIDE
        values = super().default_get(default_fields)

        lifetime_id = values.get('lifetime_id')
        if 'lifetime_stage_id' in default_fields and lifetime_id:
            lifetime_stage = self.env['anodoo.customer.lifetime.stage'].search([('lifetime_id', '=', lifetime_id)],
                                                                               order="is_default desc, sequence, id")
            values['lifetime_stage_id'] = lifetime_stage[0].id

        return values

    # '''
    # 切换lifetime_id时，根据当前的lifetime_state_id的类型，切换到新lifetime的对应类型
    #     @api.onchange('lifetime_id')
    #     def on_change_lifetime_id(self):
    #         if not self.lifetime_id:
    #             return
    #
    #         current_stage_id = self.lifetime_stage_id
    #         change_stage_id = None
    #
    #         if not current_stage_id:
    #             if current_stage_id.is_prospect:
    #                 pass
    #             elif current_stage_id.is_losing:
    #                 pass
    #             elif current_stage_id.is_success:
    #                 pass
    #
    #         if not change_stage_id:
    #             lifetime_stage = self.env['anodoo.customer.lifetime.stage'].search([('lifetime_id', '=', self.lifetime_id)], order="is_default desc, sequence, id")
    #             self.lifetime_stage_id = lifetime_stage[0]
    #  '''

    @api.depends('lifetime_id', 'lifetime_stage_id')
    def _compute_is_prospect(self):
        for record in self:
            record.is_prospect = False

    @api.depends('lifetime_id', 'lifetime_stage_id')
    def _compute_is_losing(self):
        for record in self:
            record.is_losing = False

    @api.depends('lifetime_id', 'lifetime_stage_id')
    def _compute_is_success(self):
        for record in self:
            record.is_success = False

    @api.onchange('lifetime_id')
    def _onchange_lifetime_id(self):
        LifetimeStage = self.env['anodoo.customer.lifetime.stage']

        new_stage = None
        if self.lifetime_stage_id.is_prospect:
            lifetime_stage = LifetimeStage.search(
                [('lifetime_id', '=', self.lifetime_id.id), ('is_prospect', '=', True)], limit=1)
            if lifetime_stage:
                new_stage = lifetime_stage[0]
        elif self.lifetime_stage_id.is_losing:
            lifetime_stage = LifetimeStage.search([('lifetime_id', '=', self.lifetime_id.id), ('is_losing', '=', True)],
                                                  limit=1)
            if lifetime_stage:
                new_stage = lifetime_stage[0]
        elif self.lifetime_stage_id.is_success:
            lifetime_stage = LifetimeStage.search(
                [('lifetime_id', '=', self.lifetime_id.id), ('is_success', '=', True)], limit=1)
            if lifetime_stage:
                new_stage = lifetime_stage[0]
        if new_stage:
            self.lifetime_stage_id = new_stage
        else:
            lifetime_stage = LifetimeStage.search([('lifetime_id', '=', self.lifetime_id.id)],
                                                  order="is_default desc, sequence, id", limit=1)
            if lifetime_stage:
                self.lifetime_stage_id = lifetime_stage[0]
            else:
                self.lifetime_stage_id = LifetimeStage

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        context = self._context or {}
        customer_search_mode = context.get('customer_search_mode')
        if customer_search_mode == 'customer_my':
            args += [('user_id', '=', self.env.user.id)]


        return super()._search(args, offset, limit, order, count=count, access_rights_uid=access_rights_uid)

