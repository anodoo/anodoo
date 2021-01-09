https://www.odoo.com/page/employees-features 官方介绍page
https://blog.csdn.net/weixin_35737303/article/details/79962342
https://www.zhihu.com/question/305208554/answer/549008877

hr.employee.category 员工类型,系统上显示员工标签
hr.employee.base  虚拟类
hr.employee
hr.employee.public  设置为readonly

hr.department
hr.job

hr.plan  hr的相关流程，如入职，离职，用来管理activity
hr.plan.activity.type

一个人在多个公司任职

hr.work.entry 工作记录，是合同，休假，薪酬模块的基础
    在工资表中通过甘特图展现
state = fields.Selection([
    ('draft', 'Draft'),
    ('validated', 'Validated'),
    ('conflict', 'Conflict'),
    ('cancelled', 'Cancelled')
], default='draft')

hr.work.entry.type
hr.user.work.entry.employee
==============================================================================================
hr_attendance  考勤，一般是打卡机讲考勤数据记录到odoo中。考勤信息和工资计算的关系。

hr.attendance 比较简单，就是开始时间，结束时间。


==============================================================================================
hr_contract 合同

hr.contract  合同审批流程
hr.payroll.structure.type  薪资结构类型

==============================================================================================
hr.skills

简历
hr.resume.line.type  如教育，工作经历，实习等分类
hr.resume.line 员工的一条记录。简历包含了多个记录，按照不同的分类进行展现

技能
hr.skill.type 如开发语言技能
hr.skill 如java，c++
hr.skill.level 级别
hr.employee.skill 员工技能，如A有C++级别为高级

==============================================================================================
hr_holidays 假期管理，包括休假和公司统一安排假期



==============================================================================================
hr_recruitment  招聘

hr.recruitment.source  来源，继承utm.source ,如领英等
hr.recruitment.stage 招聘流程的阶段
hr.recruitment.degree 学历

hr.applicant 申请人 ，关键，招聘都是按照申请人，流程来执行；也可以按照岗位
hr.applicant.category 申请人分类，标签
hr.applicant.refuse.reason  拒绝的原因

==============================================================================================
hr_referral 推荐，是application


==============================================================================================
hr_payroll 薪酬  基于合同，基于工作分录



hr.payroll.structure.type 薪酬结构类型，如月工资，临时工作。
hr.payroll.structure 一个类型下有多个薪酬结构，有一个默认的

default_schedule_pay = fields.Selection([
    ('monthly', 'Monthly'),
    ('quarterly', 'Quarterly'),
    ('semi-annually', 'Semi-annually'),
    ('annually', 'Annually'),
    ('weekly', 'Weekly'),
    ('bi-weekly', 'Bi-weekly'),
    ('bi-monthly', 'Bi-monthly'),
], string='Default Scheduled Pay', default='monthly',
    help="Defines the frequency of the wage payment.")


hr.salary.rule 薪酬规则，属于某一个薪酬结构的定义
hr.salary.rule.category  薪酬规则分类，如基本工资，补助，奖金等

hr.rule.parameter 薪酬参数  用来计算的一些参数
coefficients = self.env['hr.rule.parameter']._get_parameter_from_code('tax_deduction_fuel_coefficients', raise_if_not_found=False)
hr.rule.parameter.value  参数值，根据时间定义多个版本

hr.payslip 工资条
hr.payslip.line 计算出来的明细
hr.payslip.worked_days  实际的工作天数记录
hr.payslip.input.type 其他输入类型，可以在哪些薪酬结构中使用
hr.payslip.input  具体计算薪酬中输入的值，如计算提成的销售额

hr.payslip.run 定时任务？

==============================================================================================
hr_expense
实现报销单，报销项目，流程，入账，付款等

报销负责人：一个部门的报销负责人
报销产品：报销类目，挂在哪个科目下
可以替别人报销


hr.expense 一个报销项目
state = fields.Selection([
    ('draft', 'To Submit'),
    ('reported', 'Submitted'),
    ('approved', 'Approved'),
    ('done', 'Paid'),
    ('refused', 'Refused')
]

hr.expense.sheet  一张报销单

state = fields.Selection([
    ('draft', 'Draft'),
    ('submit', 'Submitted'),
    ('approve', 'Approved'),
    ('post', 'Posted'),
    ('done', 'Paid'),
    ('cancel', 'Refused')
],


sale_expense:  针对订单，重开一部分报销的发票，并把这个费用成本挂在客户下。

hr_payroll_expense  通过工资单报销费用
hr_expense_predict_product

==============================================================================================
hr_appraisal 考评 比较独立，没有和薪酬关联

hr.appraisal.plan 公司的评估计划，到达后的6个月，或者上一个评估后的6个月。根据员工的入职时间，上一次考评时间，自动生产考评，任务，提醒等

hr.appraisal.goal 目标设置，某人，和其管理者，顶一个目标，进度，最后日期
hr.appraisal.note

hr.appraisal 主要是文字性的考评，对过程进行管理。

hr_appraisal_survey 问卷式考评

==============================================================================================
hr_timesheet
工时对外的销售，对内的计算，和考勤和假期关联
工时是通过account.analytic.line分析账户来实现