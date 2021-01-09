# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models

'''

https://blog.csdn.net/M0relia/article/details/39025947

  'category': 'Hidden',
This module provides the core of the Odoo Web Client.
/web/所有的访问应该都在这里main.py
Js,css文件很多在这里



	主要参考odoo.http
	url和controller的方法的对应，再到model的方法的对应
	富客户端
丰富的js代码量
前端和后端，就是通过call_back和json访问来实现
后续前端这一块很难去改动
	Web基础controller
Home
WebClient
Proxy
Database
Session
Dataset
View
Binary
Action
Export
ExportFormat
CSVExport
ExcelExport
ReportController
	Controller
https://www.cnblogs.com/kfx2007/p/4936156.html


'''
