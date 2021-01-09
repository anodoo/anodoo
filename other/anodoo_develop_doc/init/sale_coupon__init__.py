# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models
from . import wizard
from . import report

'''
	类别:销售
	依赖
Sale_management
	功能
销售->产品 下
基于用户,产品,以及其他条件设置优惠
可以discount,送产品,免邮费
基于program创建coupon
	实体
Sale.coupon.program
两种类型,promotion, coupon
关联一个rule,一个reward(一对一关系)
Sale.coupon.rule
Program的条件,产品或客户范围等等
Sale.coupon.reward
促销内容, dicount,产品,免邮费
Sale.coupon
生产的优惠券

扩展
Sale.order
Sale.order.line


select * from sale_coupon_program;

select * from sale_coupon_rule;
select * from sale_coupon_reward;

select * from sale_coupon;
select * from sale_coupon_apply_code;  申请使用coupon code记录
select * from sale_coupon_generate;; program生成coupon记录

'''
