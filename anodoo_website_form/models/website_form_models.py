# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WebsiteForm(models.Model):
    _name = "anodoo.website.form"
    _description = "通用的网站表单"
    _order = "id desc"

    type = fields.Char('类型', help="用来区分不同的表单")

    name = fields.Char('名称')

    description = fields.Text('说明')

    number_field = fields.Integer('数字', help="用来存储数字型")

    date_field = fields.Date('日期')

    date_time_field = fields.Datetime('日期时间')

    custom_data = fields.Text('自定义数据', help="用来存放自定义字段的内容")

    attachment_ids = fields.One2many('ir.attachment', compute='_compute_attachment_ids', string="附件", readonly=False)

    def _compute_attachment_ids(self):
        for form in self:
            form.attachment_ids = self.env['ir.attachment'].search(
                [('res_id', '=', form.id), ('res_model', '=', 'anodoo.website.form')])