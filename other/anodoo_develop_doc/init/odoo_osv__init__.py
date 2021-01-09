# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import osv

# 	Osv 应该废弃，orm代替
# 	class oldmodel（osv.osv）:


'''

1. Domain
https://www.cnblogs.com/wanxiangIT/p/10337129.html
操作符       	说明        
=,>.<,>=,<=,!=	比较运算，等于，不等于，大于，大于等于，小于，小于等于
like  	模糊匹配，通过%value%匹配     
=like	可以使用模式匹配，下划线-匹配一个字符，百分号%匹配零或者多个字符    
ilike   	类似like，但是忽略大小写
=ilike     	类似=like，但是忽略大小写  
not like	通过%value%不匹配的     
not ilike     	类似not like，但是忽略大小写
=?     	未设置或者等于，未设置表示当值是None或者是False，其余和=一样     
in	判断value是否在元素的列表里面     
not in    	判断value是否不再元素的列表里面
child_of     	判断是否value的子录,  [(A,'child_of',A)]返回true
 
2. Expression.py
l 构建表达式
l Domain表达式
n Odoo domain写法及运用
u https://segmentfault.com/a/1190000014758701
n 波兰表示法
u https://www.cnblogs.com/wanxiangIT/p/10337129.html
n  
n Domain operator
n Domain term
n Domain leaf
 
3. Query.py
查询
'''