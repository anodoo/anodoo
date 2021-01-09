'''
Created on 2019年11月25日

@author: lionger
'''
from odoo import models, fields
from serial.tools.list_ports_windows import string
from odoo import models, fields, api

from odoo.addons.crm.models import crm_stage
from anodoo_lead.models import crm_stage
from . import crm_stage

'''
_register    要创建不被实例化的类，可设置  _register属性为 False。
_auto = False 用于是否应创建数据表(默认值: True)。若设置为 False，可重写 init() 来创建数据表。
_table = None 若设置为 _autoSQL表名由模型所使用 
_sequence = None 用于ID字段的SQL排序 
_sql_constraints = [] SQL 约束 [(name, sql_def, message)] 
_register = True 在ORM中不可见 
_name = None 模型名 (点标记法，模块命名空间) 
_description = None 模型的非正式名称 
_inherit = None 继承自Python的模型, str or list(str)
_inherits = {} 字典 {‘parent_model’: ‘m2o_field’}

_rec_name = None 对标签记录所使用的字段，默认值： name 
_order = 'id' 对搜索结果的默认排序字段

_check_company_auto = False 在写入和创建时，调用_check_company 来确保以check_company=True 为属性的关联字段的公司一致性。 
_parent_name = 'parent_id' 用于父级字段的many2one字段 
_parent_store = False 为计算parent_path字段设置为True。

_date_name = 'date' 默认日历视图所使用的字段 
_fold_name = 'fold' 看板视图中决定折叠分组的字段
'''
class ModelDemo(models.Model):
    
    _name = "anodoo.model.demo"
    _description = "model demo"
    _order = "id desc"
    _inherit = ['mail.activity.mixin']
    
    _register = False
    
    '''
string (str) – 用户所能看到的字段标签，如未设置，ORM会接收类（首字母大写）中的字段名。
help (str) – 用户所能看到的字段提示信息
readonly (bool) –字段是否为只读(默认值： False)。仅对 UI 产生影响。代码中的任意字段分配都会起作用(如果字段是一个存储字段且可推导（inversable）).
required (bool) – 字段值是否为必填 (默认值: False)
index (bool) – 字段在数据库中是否进行了索引。注：对非存储及虚拟字段不产生影响。 (默认值： False)
default (value 或 callable) – 字段的默认值；可以是静态值，或接收记录集并返回值的函数；使用 default=None 来抛弃字段的默认值。
states (dict) – 映射状态值到UI属性值对列表的字典；可选的属性有：readonly, required, invisible.
groups (str) – 组xml id (字符串)的逗号分隔列表；它限制仅组内的用户才可访问字段。
company_dependent (bool) –字段值是否依赖于当前公司；值不存储在模型表中。它注册为 ir.property。在需要用到company_dependent字段的值时，会搜索关联当前公司（在属性存在的话搜索当前记录）的ir.property 。如果值在记录中发生变化，这要么会修改当前记录（若存在）中的已有属性，.要么为当前公司及res_id新建一个属性。如果在公司端发生了值的改变，它会影响值未生改变的所有记录。
copy (bool) – 在复制记录时是否应拷贝该字段值(默认: 普通字段为True， one2many 及计算字段，包含属性字段及关联字段，为False)
store (bool) – 字段是否存储在数据库中 (默认:True, 对于计算字段为False)

compute (str) –计算该字段的方法名
compute_sudo (bool) – 字段是否应超越权限以超级用户进行重新计算 (对于存储字段默认为 True，对于非存储字段默认为 False )
inverse (str) – 推导字段的方法名（可选参数）
search (str) – 实现对字段搜索的方法名 (可选参数)
related (str) – 字段名的序列
    '''
    
    is_ok = fields.Boolean('布尔', default=True)
    
    meeting_count = fields.Integer('整数')
    sequence = fields.Integer('排序', default=10)
    
    '''
    digits (tuple(int,int) or str) – 一个(总数, 小数位)对或 或引用 decimal.precision 记录的字符串。
    '''
    day_open = fields.Float("小数", digits=(5,2))
    '''
    currency_field (str) – 存储用于表述这一倾向字段的币种的字段名 (默认为: 'currency_id')
    '''
    revenue = fields.Monetary('货币', currency_field='company_currency')
    
    '''
    size (int) – 针对该字段所存储值的最大的大小
    trim (bool) – 描述值是否进行去两边空格的操作 (默认值为 True)。注意 trim 操作仅由网页客户端所应用。
    translate (bool or callable) – 启用对字段值的翻译；使用 translate=True 来整体翻译字段值；translate 也可由 translate(callback, value) 等可调用方法所调用，它通过使用 callback(term)来获取词汇的翻译来进行value的翻译。
    '''
    name = fields.Char('Name', required=True)
    email_from = fields.Char('Email', help="Email address of the contact", tracking=40, index=True)
    website = fields.Char('Website', index=True, help="Website of the contact")
    description = fields.Text('说明')
    
    date = fields.Date('日期')
    date_action_last = fields.Datetime('日期时间', readonly=True)
    
    
    '''
    selection (list(tuple(str,str)) 或 callable 或 str) – 指定这个字段可能的值。它要么给定一个 (value, label)对的列表，要么是一个模型方式或方法名。属性selection 在related 或扩展字段以外的情况下是都是必须的。
    selection_add (list(tuple(str,str))) –在重载字段的情况下提供对选项的一个扩展。是一个 (value, label) 对的列表或单值元组 (value,)，其中的值必须要出现在重载选项中。
    '''
    type = fields.Selection([('customer', '面向客户'), ('product', '面向产品')], required=True,
        string='', default='customer', help="")
    type = fields.Selection([('lead', 'Lead'), ('opportunity', 'Opportunity')], index=True, required=True, tracking=15,
        default=lambda self: 'lead' if self.env['res.users'].has_group('crm.group_use_lead') else 'opportunity',
        help="Type is used to separate Leads and Opportunities")
    
    
    '''
    comodel_name (str) – 目标模型Mandatory 除关联或扩展字段以外的名称。
    domain – 在客户端（域或字符串）设置备用值的可选域
    context (dict) – 在处理该字段时用于客户端的可选上下文
    ondelete (str) – 在引用的记录被删除时所做的操作：可用的值下有： 'set null'(默认）, 'restrict', 'cascade'
    auto_join (bool) – 对该字段的搜索是否有JOIN生成 (默认值：False)
    delegate (bool) – 设置为True 来让你目标模型的字段可通过当前模型进行访问(对应 _inherits)
    check_company – 添加默认作用域['|', ('company_id', '=', False), ('company_id', '=', company_id)]。 标记该字段在 _check_company中进行验证。
    '''
    partner_id = fields.Many2one('res.partner', string='Customer', tracking=10, index=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", help='')
    
    '''
    comodel_name (str) – name of the target model
    inverse_name (str) – name of the inverse Many2one field in comodel_name
    domain – an optional domain to set on candidate values on the client side (domain or string)
    context (dict) – an optional context to use on the client side when handling that field
    auto_join (bool) – whether JOINs are generated upon search through that field (default: False)
    limit (int) – optional limit to use upon read
    '''
    onemany = fields.One2many('res.partner', 'partner_id', string='伙伴')
    
    '''
    comodel_name – name of the target model (string) mandatory except in the case of related or extended fields
    relation (str) – optional name of the table that stores the relation in the database
    column1 (str) – optional name of the column referring to “these” records in the table relation
    column2 (str) – optional name of the column referring to “those” records in the table relation
    '''
    tag_ids = fields.Many2many('crm.lead.tag', 'crm_lead_tag_rel', 'lead_id', 'tag_id', string='多对多关系', help='帮助信息')
    
    create_uid = fields.Many2one(string='Created by')
    create_date = fields.Datetime(string='Created on')
    write_uid = fields.Many2one(string='Last Updated by')
    write_date = fields.Datetime(string='Last Updated on')
    display_name = fields.Char(string='Display Name') #_compute_display_name
    

树状对象  class CustomerLabelCategory in customer_segment
阶段对象  class CustomerLifetimeStage in customer_lifetime
属性对象 CustomerType,  标签对象CustomerLabel, 日志对象CustomerAllot

#继承
class Customer(models.Model):	
    _inherit = 'res.partner'

#新简单对象
class Customer(models.Model):
	_name = ''
	_description = ''
	_rec_name = 'name'
    _order = 'id'
	
    
    name = fields.Char('名称', required=True)
    
    sequence = fields.Integer('序号', default=10)
    
    description = fields.Text('描述')
    
    #其他常用字段
    active = fields.Boolean('激活', default=True)
    
    customer_identity = fields.Char('唯一标识信息', help='客户唯一标识信息')
    
    is_default = fields.Boolean('是否默认', default=False)
    
    customer_id = fields.Many2one('res.partner', string='客户1', help='客户与客户的关系的主方')
    
    manage_user_id = fields.Many2one('res.users', string='管理员')
    
    fold = fields.Boolean('合并', default=False)
    
    customer_type = fields.Selection([('company', '公司客户'), ('person', '个人客户'), ('family', '家庭客户')], 
                           string='客户性质', default='company', help='客户类型定义，可扩展')
                           
   	customer_priority = fields.Selection([('0', 'Low'),  ('1', 'Medium'),  ('2', 'High'), ('3', 'Very High')], 
   	string='优先级', index=True, default='0')
       
    resume_line_ids = fields.One2many(related='employee_id.resume_line_ids', readonly=False)
       
    @api.model
    def default_get(self, fields):
        ctx = dict(self.env.context)
        if ctx.get('default_team_id') and not ctx.get('crm_team_mono'):
            ctx.pop('default_team_id')
        return super(Stage, self.with_context(ctx)).default_get(fields)
    
    @api.model
    def default_get(self, fields):
        vals = super(AccountBankStmtCashWizard, self).default_get(fields)
        balance = self.env.context.get('balance')
        statement_id = self.env.context.get('statement_id')
        if 'start_bank_stmt_ids' in fields and not vals.get('start_bank_stmt_ids') and statement_id and balance == 'start':
            vals['start_bank_stmt_ids'] = [(6, 0, [statement_id])]
        if 'end_bank_stmt_ids' in fields and not vals.get('end_bank_stmt_ids') and statement_id and balance == 'close':
            vals['end_bank_stmt_ids'] = [(6, 0, [statement_id])]

        return vals
    
    @api.depends('cashbox_lines_ids', 'cashbox_lines_ids.coin_value', 'cashbox_lines_ids.number')
    def _compute_total(self):
        for cashbox in self:
            cashbox.total = sum([line.subtotal for line in cashbox.cashbox_lines_ids])
            #stage.team_count = self.env['crm.team'].search_count([])
            
    @api.model_create_multi
    def create(self, vals):
        cashboxes = super(AccountBankStmtCashWizard, self).create(vals)
        cashboxes._validate_cashbox()
        return cashboxes

    def write(self, vals):
        res = super(AccountBankStmtCashWizard, self).write(vals)
        self._validate_cashbox()
        return res
    
    @api.depends('attribute_line_ids.active', 'attribute_line_ids.product_tmpl_id')
    def _compute_products(self):
        for pa in self:
            pa.product_tmpl_ids = pa.attribute_line_ids.product_tmpl_id

get_param = request.env['ir.config_parameter'].sudo().get_param
get_param('auth_signup.reset_password')
    

action = self.env.ref('base.action_res_users').read()[0]

raise NotImplementedError("")
    


    
    
    _cr = property(lambda self: self.env.cr)
    _uid = property(lambda self: self.env.uid)
    _context = property(lambda self: self.env.context)
self.env['account.journal'].browse

program = self.env['sale.coupon.program'].browse(self.env.context.get('active_id'))

        vals = {'program_id': program.id}

for count in range(0, self.nbr_coupons):

for partner in self.env['res.partner'].search(safe_eval(self.partners_domain)):
	vals.update({'partner_id': partner.id})

subject = '%s, a coupon has been generated for you' % (partner.name)

template = self.env.ref('sale_coupon.mail_template_sale_coupon', raise_if_not_found=False)

template.send_mail(coupon.id, email_values={'email_to': partner.email, 'email_from': self.env.user.email or '', 'subject': subject,})

getattr(self, field)


tags and [unslug(tag)[1] for tag in tags.split(',')] or []
    
            try:
            except Exception:
            print('ab')
            return (None, None)
        
设置数据和读取
generate_lead_from_alias = fields.Boolean('Manual Assignation of Emails', config_parameter='crm.generate_lead_from_alias')
pls_threshold = int(self.env['ir.config_parameter'].sudo().get_param('crm.pls_rebuild_threshold'))

self.env['ir.config_parameter'].sudo().set_param('crm.pls_rebuild_threshold', 0)

next_type_ids = fields.Many2many(
        'mail.activity.type', 'mail_activity_rel', 'activity_id', 'recommended_id',
        domain="['|', ('res_model_id', '=', False), ('res_model_id', '=', res_model_id)]",
        string='Recommended Next Activities')
    previous_type_ids = fields.Many2many(
        'mail.activity.type', 'mail_activity_rel', 'recommended_id', 'activity_id',
        domain="['|', ('res_model_id', '=', False), ('res_model_id', '=', res_model_id)]",
        string='Preceding Activities')
相关关系的定义方式

字段的states的使用方法
name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, states={'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))

self._install_module('payment_paypal')
代码里安装模块