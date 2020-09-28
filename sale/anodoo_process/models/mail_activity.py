# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MailActivityType(models.Model):
    
    _inherit = "mail.activity.type"
    
    category = fields.Selection(selection_add=[
        ('email_send', '发送邮件'),
        ('email_receive', '接收邮件'),
        ('event', '参加活动'),
        ('sms_send', '发送短信'),
        ('sms_receive', '接收短信'),
        ('website_visit', '访问网站'),
        ('website_page', '浏览网页'),
        ('website_review', '评论网页'),
        ('website_livechat', '在线聊天'),
        ('blog_push', '推送文章'),
        ('blog_visit', '浏览文章'),
        ('blog_add', '收藏文章'),
        ('blog_review', '评论文章'),
        ('forum_visit', '浏览帖子'),
        ('forum_create', '发表帖子'),
        ('forum_review', '回复帖子'),
        ('elearning_push', '推送在线课程'),
        ('elearning_join', '参加在线课程'),
        ('elearning_review', '评论在线课程'),
        ('prm_signup', '注册代理商'),
        ('prm_oppor', '分派商机'),
        ('ecomm_recommond', '电商推荐'),
        ('ecomm_shopping', '电商购物'),
        ('ecomm_pay', '电商支付'),
        ])
    
    opportunity_lifetime_id = fields.Many2one('anodoo.opportunity.lifetime', string='生命周期', help="活动和商机的阶段进行关联")
    
    stage_id = fields.Many2one('crm.stage', string="阶段", domain="[('opportunity_lifetime_id','=', opportunity_lifetime_id)]", help="针对商机特定阶段定义的活动")
    
    is_inner = fields.Boolean('是否内部活动', default=False)
    
    is_passive = fields.Boolean('是否被动活动', default=False)
    
    
    
#     @api.depends('res_model', 'res_id')
#     def _compute_lifetime(self):
#         for activity in self:
#             activity.lifetime_id = activity.res_model and activity.res_model=='crm.lead' and \
#                 self.env[activity.res_model].browse(activity.res_id).lifetime_id
                

class MailActivity(models.Model):
    
    _inherit = "mail.activity"
    
    stage_id = fields.Many2one('crm.stage', string="阶段", related="activity_type_id.stage_id", store=True)
    
    color = fields.Integer('Color Index', default=0)