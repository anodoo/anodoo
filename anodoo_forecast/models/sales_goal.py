# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError



class SaleGoalModel(models.Model):
    _name = 'anodoo.sales.goal.model'
    _description = '灵活的销售模型定义，可支持任意对象，字段的多种计算模式'
    _rec_name = 'name'
    _order = 'id'
    
    
    name = fields.Char('名称', required=True)
    
    sequence = fields.Integer('序号', default=10, help="序号")
    
    active = fields.Boolean('激活', default=True, tracking=True)
    
    description = fields.Text('描述', translate=False)
    
    model_id = fields.Many2one('ir.model', string='业务对象', help='计算目标值的业务对象')
    
    model_name = fields.Char(related='model_id.model')
    
    field_id = fields.Many2one('ir.model.fields', string='字段', tracking=10, index=True,  domain="[('model_id', '=', model_id)]", help='计算目标值的业务对象的字段')
    
    compute_domain = fields.Text(string="限制条件", default='[]', required=True, help="目标针对业务对象进行计算的限制条件")
    
    compute_type = fields.Selection([('sum', 'Sum合计'), ('count', 'Count数量'), ('huanbi', '环比'), ('tongbi', '同比')], required=True,
        string='计算方式', default='sum', help="模型的计算方式")
    
    dimension_field_ids = fields.One2many('anodoo.sales.goal.breakdown.dimension.field', 'goal_model_id', string='分解纬度对应字段')
    
    def compute_goal(self):
        '''
        
        '''
        pass

BREAKDOWN_DIMENSION_BUSINESS_TYPE = [('territory', '销售区域'), ('team', '销售团队'), 
                            ('salesperson', '销售员'), ('customer', '客户'), 
                            ('partner', '合作伙伴'), ('productcategory', '产品类别'), 
                            ('product', '产品')]

BREAKDOWN_DIMENSION_DATETIME_TYPE = [('year', '年'), ('quarter', '季度'), 
                            ('month', '月'), ('week', '周'), 
                            ('day', '天'), ('workday', '工作日')]


class SaleGoal(models.Model):
    _name = 'anodoo.sales.goal'
    _description = '销售目标,关联目标模型,可进行多纬度分解'
    _rec_name = 'name'
    _order = 'id'
    
    
    name = fields.Char('名称', required=True)
    
    sequence = fields.Integer('序号', default=10, help="序号")
    
    active = fields.Boolean('激活', default=True, tracking=True)
    
    description = fields.Text('描述', translate=False)
    
    goal_model_id = fields.Many2one('anodoo.sales.goal.model', string='目标模型')
    
    goal_state_id = fields.Many2one('anodoo.sales.goal.state', string='目标状态')
    
    goal_value = fields.Char('目标值', help='根据目标模型中的目标值计算类型,填写正确的目标值,如整数,小数,百分比数等')
    
    result_value = fields.Char('目标完成值')
    
    begin_date = fields.Date('开始日期')
    
    end_date = fields.Date('结束日期')
      
    relation_ids = fields.One2many('anodoo.sales.goal.breakdown.dimension.relation', 'goal_id', string='目标分解', help='一个目标可以按照多个分解纬度来分解')

    
    
class SaleGoalState(models.Model):   
    _name = 'anodoo.sales.goal.state'
    _description = '销售目标状态'
    _rec_name = 'name'
    _order = "sequence, id"
    
    
    name = fields.Char('名称', required=True)
    
    sequence = fields.Integer('序号', default=10, help="序号")
    
    fold = fields.Boolean('合并', default=False)
    
    description = fields.Text('描述', translate=False)
    
    
class SaleGoalBreakdown(models.Model):   
    _name = 'anodoo.sales.goal.breakdown'
    _description = '销售目标分解'
    _rec_name = 'name'
    _order = 'id'
    _parent_store = True
    

     
    name = fields.Char(string='分解名称')
    
    active = fields.Boolean('激活', default=True, tracking=True)
    
    description = fields.Text('描述', translate=False)
    
    goal_id = fields.Many2one('anodoo.sales.goal', string='销售目标')
    
    dimension_id = fields.Many2one('anodoo.sales.goal.breakdown.dimension', string='分解纬度', domain=lambda self: self._get_dimensions_by_goal())
        
    dimension_type = fields.Selection([('business', '业务纬度'), ('datetime', '时间纬度')], string='分解纬度类型', help="销售目标可以按照时间纬度,业务纬度进行分解")
    
    business_type = fields.Selection(BREAKDOWN_DIMENSION_BUSINESS_TYPE, string='业务纬度类型', help="按照业务纬度分解目标")
    
    datetime_type = fields.Selection(BREAKDOWN_DIMENSION_DATETIME_TYPE, string='时间纬度类型', help="按照时间纬度分解目标")
    
    parent_id = fields.Many2one('anodoo.sales.goal.breakdown', string='父分解', index=True, ondelete='cascade')
    child_ids = fields.One2many('anodoo.sales.goal.breakdown', 'parent_id', string='子分解')

    parent_path = fields.Char(index=True)
        
    owner_territory_id = fields.Many2one('anodoo.sales.territory', string='销售区域')
    owner_team_id = fields.Many2one('crm.team', string='销售团队')
    owner_salesperson_id = fields.Many2one('res.users', string='销售员')
    owner_customer_id = fields.Many2one('res.partner', string='客户')
    owner_product_category_id = fields.Many2one('product.category', string='产品类别')
    owner_product_template_id = fields.Many2one('product.template', string='产品')
    
    owner_year = fields.Char('年')
    owner_quarter = fields.Char('季度')
    owner_month = fields.Char('月')
    owner_week = fields.Char('周')
    owner_day = fields.Char('天')
    owner_workday = fields.Char('工作日')
    
    owner_name = fields.Char('分解对象', compute='_compute_owner_name')
    
    
    owner_user_id = fields.Many2one('res.users', string='负责人', help='目标最终的负责人')
    
    breakdown_goal_value = fields.Char('分解目标值')
    
    result_value = fields.Char('目标完成值')

    #     BREAKDOWN_DIMENSION_BUSINESS_TYPE = [('territory', '销售区域'), ('team', '销售团队'), 
#                             ('salesperson', '销售员'), ('customer', '客户'), 
#                             ('partner', '合作伙伴'), ('productcategory', '产品类别'), 
#                             ('product', '产品')]
# BREAKDOWN_DIMENSION_DATETIME_TYPE = [('year', '年'), ('quarter', '季度'), 
#                             ('month', '月'), ('week', '周'), 
#                             ('day', '天'), ('workday', '工作日')]
    #@api.depends('dimension_type', 'business_type', 'datetime_type')
    @api.model
    def _get_owner_name(self, breakdown):
        breakdown_name = ''
        if breakdown.dimension_type == 'business':
            if breakdown.business_type == 'territory':
                breakdown_name = breakdown.owner_territory_id.name
            elif breakdown.business_type == 'team':
                breakdown_name = breakdown.owner_team_id.name
            elif breakdown.business_type == 'salesperson':
                breakdown_name = breakdown.owner_salesperson_id.name
            elif breakdown.business_type == 'customer':
                breakdown_name = breakdown.owner_customer_id.name 
            elif breakdown.business_type == 'productcategory':
                breakdown_name = breakdown.owner_product_category_id.name 
            elif breakdown.business_type == 'product':
                breakdown_name = breakdown.owner_product_template_id.name 
            else:
                breakdown_name = ''
        else:
            if breakdown.datetime_type == 'year':
                breakdown_name = breakdown.owner_year
            elif breakdown.datetime_type == 'quarter':
                breakdown_name = breakdown.owner_quarter
            elif breakdown.datetime_type == 'month':
                breakdown_name = breakdown.owner_month
            elif breakdown.datetime_type == 'week':
                breakdown_name = breakdown.owner_week
            elif breakdown.datetime_type == 'day':
                breakdown_name = breakdown.owner_day
            elif breakdown.datetime_type == 'workday':
                breakdown_name = breakdown.owner_workday
            else:
                breakdown_name = ''
        return breakdown_name
                        
    def _compute_owner_name(self):
        for breakdown in self:
            breakdown.owner_name = self._get_owner_name(breakdown)

    def _get_dimensions_by_goal(self):
        dimensions = []
        if self.goal_id :
            relations = self.env['anodoo.sales.goal.breakdown.dimension.relation'].search([('goal_id', '=', self.goal_id.id)])
        
            for relation in relations:
                dimensions.append(relation.dimension_id)
        
        return dimensions
        
    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        if self._context.get('list_my'):
            args += [('owner_user_id', '=', self.env.uid)]
        
        return super()._search(args, offset=offset, limit=limit, order=order, count=count, access_rights_uid=access_rights_uid)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            name = vals.get('name')
            if not name:                
                vals.update({'name':name})
        
        return super().create(vals_list)

class SaleGoalBreakdownDimension(models.Model):   
    _name = 'anodoo.sales.goal.breakdown.dimension'
    _description = '销售目标分解纬度'
    _rec_name = 'name'
    _order = 'id'    
    _parent_store = True
    
    
    
    parent_id = fields.Many2one('anodoo.sales.goal.breakdown.dimension', string='父纬度', index=True, ondelete='cascade')
    child_ids = fields.One2many('anodoo.sales.goal.breakdown.dimension', 'parent_id', string='子纬度')

    @api.model
    def _default_name(self):
        return self.parent_id.name if self.parent_id else ''
    
    name = fields.Char(string='纬度名称', default=_default_name)
    
    parent_path = fields.Char(index=True)
    
    dimension_type = fields.Selection([('business', '业务纬度'), ('datetime', '时间纬度')], default='business', string='分解纬度类型', help="销售目标可以按照时间纬度,业务纬度进行分解")
    
    business_type = fields.Selection(BREAKDOWN_DIMENSION_BUSINESS_TYPE, string='业务纬度类型', help="按照业务纬度分解目标")
    
    datetime_type = fields.Selection(BREAKDOWN_DIMENSION_DATETIME_TYPE, string='时间纬度类型', help="按照时间纬度分解目标")
    
#     @api.depends('dimension_type', 'business_type', 'datetime_type')
#     def _compute_name(self):
#         for dimension in self:
#             field_name = 'business_type' if dimension.dimension_type=='business' else 'datetime_type'
#             field_value = dimension.business_type if dimension.dimension_type=='business' else dimension.datetime_type
#             dimension_name = dict(self._fields.get(field_name).selection).get(field_value)
#             dimension.name = dimension_name
            
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
            return super(SaleGoalBreakdownDimension, self).name_get()

        res = []
        for dimension in self:
            names = []
            current = dimension
            while current:
                names.append(current.name)
                current = current.parent_id
            res.append((dimension.id, ' / '.join(reversed(names))))
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
    
class SaleGoalBreakdownDimensionRelation(models.Model):   
    _name = 'anodoo.sales.goal.breakdown.dimension.relation'
    _description = '销售目标,分解纬度,分解三者的关系,一个销售目标支持几个分解纬度,就有几个分解'
    _rec_name = 'dimension_id'
    _order = 'id'    
    
    goal_id = fields.Many2one('anodoo.sales.goal', string='销售目标', required=True)
    
    dimension_id = fields.Many2one('anodoo.sales.goal.breakdown.dimension', string='分解纬度', required=True, domain="[('child_ids', '=', False)]")
    
    breakdown_id = fields.Many2one('anodoo.sales.goal.breakdown', string='目标分解')
    
class SaleGoalBreakdownDimensionField(models.Model):   
    _name = 'anodoo.sales.goal.breakdown.dimension.field'
    _description = '销售目标分解纬度和业务对象的字段的关联'
    _rec_name = 'field_id'
    _order = 'id'
    
    goal_model_id = fields.Many2one('anodoo.sales.goal.model', string='目标模型')
    
    dimension_id = fields.Many2one('anodoo.sales.goal.breakdown.dimension', string='分解纬度')
    
    model_id = fields.Many2one('ir.model', related='goal_model_id.model_id', string='业务对象', help='计算目标值的业务对象')
    
    field_id = fields.Many2one('ir.model.fields', string='字段', domain='[("model_id", "=", model_id)]')
    
    relate_field_info = fields.Char('关联字段信息')
    
class SaleGoalBreakdownResult(models.Model):   
    _name = 'anodoo.sales.goal.breakdown.result'
    _description = '销售目标分解的考核结果'
    _rec_name = 'goal_breakdown_id'
    _order = 'id'
    
    goal_breakdown_id = fields.Many2one('anodoo.sales.goal.breakdown', string='目标分解')
    
    result_value = fields.Char('分解目标考核值')
    
    compute_time = fields.Datetime('计算时间')
    