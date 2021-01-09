from . import controllers
from . import models

'''
	落地页
	 
	l 功能
		n 讲一个实体和website的一个form对应起来
	l 依赖
		n Website
		n Mail
	l 实体
		n 扩展
			u Ir.model  那些model可以支持在form builder中使用
			u Ir.model.fields 哪些字段可以用
	l 相关
		n Website_form_project 项目任务
	 
	l 开发
		n 在所有的xml中搜索website_form_key
	 
	select * from ir_model where website_form_access is True
	 
	直接下载附件
	http://www.huangsiwei.com/web/content/2256/anodoo-20200427.tar
	 
	ebsite_form
	 
	配置实体:website_sale    data.xml  L55, 包括实体可以被form使用,以及哪些字段开放.
	website_sale_form_editor.js,  website_sale_form.xml  初始form定义,并通过js引入.
	再引入到editor体系:website.assets_editor
	通过统一的main.py读取数据(@http.route('/website_form/<string:model_name>'),包括批判开放字段,自定义字段,metadata等,然后保存到实体.custom字段如果设置了,则保存到对应字段,否则保存到message中
	 
	附件问题
	select * from ir_attachment where res_model='anodoo.website.form'
	字段
	get_authorized_fields
	感谢页面
	data-success_page
	 
	其他表单 
	website_crm_editor.js
	website_form_project.xml
	website_hr_recruitment.xml
	website_form.xml
	website_sale_form.xml

'''
