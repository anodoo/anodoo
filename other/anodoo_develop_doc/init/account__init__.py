

'''

https://www.odoo.com/page/billing
依赖“'depends' : ['base_setup', 'product', 'analytic', 'portal', 'digest'],”
Analytic 分析会计
Product

相关模块
Account_payment


	实体
	account.root
	account.group
	
	account.account
	account.account.type
	account.account.tag
	
	account.journal.group
	account.journal
	
	res.partner.bank
	
	account.analytic.line
	account.cashbox.line
	
	account.bank.statement
	account.bank.statement.line
	account.bank.statement.cashbox
	account.cash.rounding


	Account.payment 付款
	account.payment.method
	account.payment.register
	
	Account_payment_term 付款条款
	account.payment.term.line
	
	account.tax.group
	
	Account.tax 税率
	
	account.tax.report.line
	account.tax.repartition.line
	
	account.fiscal.year
	Account.fiscal.postion 税科目调整
	account.incoterms 贸易条款
	Account.journal 客户发票,凭证
	Account.reconcile.mode 核销模型
	
	account.partial.reconcile
	account.full.reconcile
	
	Account.tax.report.line 税务报告
	
	Account.move 账单,退款,入库，任务财务的移动，都涉及
        会计凭证的概念，是从一个account到另一个account的move移动
	Account.move.line
        会计分录，一个移动是复式记账，所以一边增加，另一个对应几条记录来记录减少
	
	扩展
	Res.company
	Digest.digest
	Product
	Product.templet

account_accountant

account是Invoice，这个是Accounting，一个是开票，一个是会计。
安装这个后，会修改原来account的菜单。
创建的菜单
 Accounting
Accounting/Accounting/Actions/Lock Dates  锁定会计期间
Accounting/Accounting/Actions/Reconciliation  对账
Accounting/Configuration/Accounting/Account Groups  科目组
Accounting/Configuration/Accounting/Account Tags  科目标签 account.account.tag 实体在account中定义
Accounting/Configuration/Accounting/Fiscal Years  没看到菜单，在配置中设置财年

实体

account.fiscal.year
account.reconciliation.widget

相关模块
account_bank_statement_import  14新加。以及其他4个子模块，实现银行对账单导入
account_reports 财务报告
    account_asset 管理一个公司或一个人拥有的资产。 跟踪贬值的，并创建相应的会计凭证。
        https://www.odoo.com/documentation/user/14.0/zh_CN/accounting/payables/supplier_bills/assets.html  官方操作手册
        http://www.360doc.com/content/18/0320/14/5331635_738720037.shtml  几种折旧方法说明
    account_consolidation  财务合并
    account_reports_cash_basis
    Intrastat Reports
        system for collecting information and producing statistics related to the trade in goods between the countries of the EU
    document_account:
    account_followup

account_budget 预算,是对收入和支出的预算
统计特定分析账户下（也可以没有），特定科目类型的收入或者支出

account.budget.post  对应多个会计科目
crossovered.budget
crossovered.budget.lines
    planned_amount 收入为正，支出为付
    line.practical_amount 实际的
    line.theoritical_amount 理论的，更多是这两个数的比较，和planned_amount是什么关系

You have to enter at least a budgetary position or analytic account on a budget line.
分析账户上带有会计科目？
'''
