import logging
import sys
import os

import odoo

from .command import Command, main

from . import cloc
from . import deploy
from . import scaffold
from . import server
from . import shell
from . import start


#odoo.cli.main()
#通过L7，在import command时，读入所有的command类型，然后根据命令中的参数，确定调用哪个
#基类是：Command = CommandType('Command', (object,), {'run': lambda self, args: None})，重点在run方法
#主要是server类，默认的
#templates中，可以改为anodoo自己的module结构， 参考Odoo模块目录结构：https://www.jianshu.com/p/d7293eb127c9

#
# l Command
# 	n Help
# 	n Deploy
# 		u 在odoo中deploy一个module
# 	n Scaffold
# 		u 通过模板，生成一个module
# 		u 借助jinja2
# 			l Jinja2是基于python的模板引擎，功能比较类似于于PHP的smarty，J2ee的Freemarker和velocity。 它能完全支持unicode，并具有集成的沙箱执行环境，应用广泛。jinja2使用BSD授权。
# 			l https://www.jianshu.com/p/c4cd99ee4fac
# 			l https://palletsprojects.com/p/jinja/
# 			l https://palletsprojects.com/
# 			l Armin Ronacher
# 		u L83：class template 模板功能
# 			l Cli.templates
# 		u  
# 	n Server
# 		u 服务启动
# 			l 有个main函数  L124
# 			l Server.run直接调用main函数
# 			l L172：Main函数调用odoo.service.server.start启动服务
# 		u L36：用root启动会警告
# 		u L43：db_user设置为postgres会直接退出
# 		u L78:pidfile:将pid写入pidfile文件中？
# 		u  
# 	n Shell
# 		u 命令行执行odoo
# 		u 对python，ipython等的支持
# 		u 参考python的解释器功能
# 	n Start
# 		u 快速启动server，快在哪里？
# 		u 调用server的main函数
# l Command
# 	n Main函数
# 		u 有一个commands
# 		u 判断是哪个command
# 		u 调用command的run方法
# 	n Class CommmandType(type)这个定义什么意思？
# 	n L20：  Command = CommandType（）这是一个实例，还是一个类？
# 定义了run方法
