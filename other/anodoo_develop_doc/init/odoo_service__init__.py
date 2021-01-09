# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import common
from . import db
from . import model
from . import wsgi_server
from . import server

#.apidoc title: RPC Services

""" Classes of this module implement the network protocols that the
    OpenERP server uses to communicate with remote clients.

    Some classes are mostly utilities, whose API need not be visible to
    the average user/developer. Study them only if you are about to
    implement an extension to the network protocols, or need to debug some
    low-level behavior of the wire.
"""

#rc = odoo.service.server.start(preload=preload, stop=stop)  ，主要的函数，preload为预load的数据库，
#这里是odoo作为服务端的
#先load_server_wide_modules，load base，web模块
#
# 根据情况启动不同的server：Servers: Threaded（默认的）, Gevented and Prefork, 他们都继承自CommonServer
#因为odoo服务器有三种模式——prefork, gevented, threaded，首先得大致了解一下这三种MPM（Multi-Processing Module，多进程处理模块）模式的特点，可以参考一篇关于apache服务器的博文：    http://blog.jobbole.com/91920/
# Worker ,子类WorkerHTTP, WorkerCron, 也就是有http，cron不同的线程
#启动WSGI服务，Werkzurg
#启动watch功能，实现reload的dev模式
#最后调用prefork, gevented, threaded几种server的  run（）
#   run()调用 http_spawn，启动wsgi，监听http

#   同时通过preload_registries, 安装数据库


#
# 1. Server.py
# l Start函数， L1214
# n 根据不同的形式，event，work，prefork等启动
# n 启动watchdog
# n 创建一个特定类型的Server，如ThreadedServer，调用其run函数
# n 装载modules（参考module）
# n 启动WSGI服务器
# n  
# l Werkzeug WSGI Server
# n L93 开始的几个类
# l CommonServer
# n ThreadedServer
# n GeventServer
# n PreforkServer
# l Worker  worker模式多线程
# n WorkerHTTP
# n WorkerCron
# l FSWatcherBase  监控服务文件系统，刷新重启系统
# n FSWatcherWatchdog
# n FSWatcherInotify
# l Watchdog
# n https://pypi.org/project/watchdog/
# n https://blog.csdn.net/chdhust/article/details/50514391
# n Inotify
# u https://www.cnblogs.com/sevck/p/5209487.html
# 2. Common.py
# l L57 dispatch方法
# n 通过exp_method_name调用本类中的其他方法
# u Login
# u Authenticate
# u Version
# u About
# Set_loglevel