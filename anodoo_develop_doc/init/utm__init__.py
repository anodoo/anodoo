# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models

'''
UTM参数的全名是Urchin Tracking Module


网页
https://www.odoo.com/zh_CN/page/link-tracker-features

https://docs.zhugeio.com/datamanager/utm_mark.html

依赖
Base, web
菜单
链接追踪 UTMs

相关
Link_tracker
实体
Utm.campaign 营销活动，有负责人
Utm.stage，阶段
Utm.tag，标签

Utm.medium
Utm.source
Mixin
Utm.mixin 那些需要被追踪的对象mixin这个

1.1.1.1.1.1.	Link_tracker
讲带有utm的信息改成短链接
给予utm创建一个url,并统计
/r/***,3位随机码


依赖
Utm
实体
Link.tracker   一个跟踪url
Link.tracker.click  点击
Link.tracker.code  编码


select * from link_tracker;
select * from link_tracker_code;
1.1.1.1.1.2.	Website_links
Website_links 可跟踪的短链接
使用分析型跟踪器（UTM）生成短链接，在营销活动中共享出去您的网页。 这些跟踪器可以在Google Analytics中用于跟踪点击次数和访问者，或者在Odoo报告中用于分析这些广告系列在潜在客户生成、相关收入（销售订单）、招聘等方面的效率和效果。


'''
