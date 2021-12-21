from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import safe_eval
    
class CustomerLabelCategory(models.Model):
    _name = "anodoo.customer.label.category"
    _description = '客户标签分类'
    _parent_store = True
    
    name = fields.Char(string='分类名称', required=True)
    
    parent_id = fields.Many2one('anodoo.customer.label.category', string='父分类', index=True, ondelete='cascade')
    child_ids = fields.One2many('anodoo.customer.label.category', 'parent_id', string='子分类')

    parent_path = fields.Char(index=True)
    
    description = fields.Text('描述', translate=False)
    
    #display_name = fields.Char(string='Display Name') 
    
    @api.constrains('parent_id')
    def _check_parent_id(self):
        if not self._check_recursion():
            raise ValidationError(_('You can not create recursive tags.'))

    def name_get(self):
        """ Return the categories' display name, including their direct
            parent by default.

            If ``context['partner_category_display']`` is ``'short'``, the short
            version of the category name (without the direct parent) is used.
            The default is the long version.
        """
        if self._context.get('partner_category_display') == 'short':
            return super(CustomerLabelCategory, self).name_get()

        res = []
        for category in self:
            names = []
            current = category
            while current:
                names.append(current.name)
                current = current.parent_id
            res.append((category.id, ' / '.join(reversed(names))))
        return res

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        if name:
            # Be sure name_search is symetric to name_get
            name = name.split(' / ')[-1]
            args = [('name', operator, name)] + args
        partner_category_ids = self._search(args, limit=limit, access_rights_uid=name_get_uid)
        return models.lazy_name_get(self.browse(partner_category_ids).with_user(name_get_uid))


    
class CustomerLabel(models.Model):
    _name = "anodoo.customer.label"
    _description = "客户标签"
    
    name = fields.Char(string='标签名称', required=True)
    
    category_id = fields.Many2one('anodoo.customer.label.category', string='标签分类')
    
    color = fields.Integer(string='颜色')
    
    is_auto = fields.Boolean('自动设置', help="如果是自动设置,则根据customers_domain定时自动计算")
    
    customers_domain = fields.Char(string="匹配客户", help="根据这些规则,自动匹配符合规则的客户具备这个标签")
        
    description = fields.Text('描述', translate=False)
    
class CustomerSegment(models.Model):
    _name = "anodoo.customer.segment"
    _description = '客户分群，客户群'
    
    name = fields.Char(string='客户分群名称', required=True)
    
    label_ids = fields.Many2many('anodoo.customer.label', string='客户标签', help='客户分群对应的客户标签，根据标签批判客户')
    
    sequence = fields.Integer('序号', default=10, help="客户分群的序号")
    
    description = fields.Text('描述', translate=False)
    
    dynamic_customer_ids = fields.Many2many('res.partner', 'anodoo_customer_segment_dynamic', 'segment_id', 'customer_id', string='动态客户列表', help='客户分群下的动态客户列表，根据标签动态计算并刷新')
    
    static_customer_ids = fields.Many2many('res.partner', 'anodoo_customer_segment_static', 'segment_id', 'customer_id', string='静态客户列表', help='客户分群下的静态客户列表',
                                    domain="[('customer_rank', '>', 0)]", store=True)
    
    segment_snapshot_ids = fields.One2many('anodoo.customer.segment.snapshot', 'segment_id', string='客户快照')
    
#     @api.depends('label_ids')
#     def _compute_dynamic_customer_ids(self):
        
            
    #前台按钮,用来刷新标签下的客户列表
    def refresh_labels_customer_list(self):
        ResPartner = self.env['res.partner']
        for record in self:
            domain = []
            for label in record.label_ids:
                if label.customers_domain:
                    domain += safe_eval(label.customers_domain)
            
            if domain:
                domain += [('customer_rank', '>', 0)]
                record.dynamic_customer_ids = ResPartner.search(domain)
        
        return True
    
    
class CustomerSegmentSnapshot(models.Model):
    _name = "anodoo.customer.segment.snapshot"
    _description = '客户快照，是客户分群的静态客户列表，它是某一个时刻对该客户分群下客户列表的一个快照。'
    
    segment_id = fields.Many2one('anodoo.customer.segment', string='客户分群')
    
    customer_count = fields.Integer('客户数量', compute='_compute_customer_count')
    
    customer_ids = fields.Many2many('res.partner', string='客户', help='客户分群下的静态客户列表',
                                    domain="[('customer_rank', '>', 0)]")
    
 
    description = fields.Text('描述', translate=False)
    
    def _compute_customer_count(self):
        for record in self:
            record.customer_count = 9283