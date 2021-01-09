# -*- coding: utf-8 -*-
# from odoo import http
import json

from odoo import http
from odoo.http import request

import datetime
import os

MODULE_MAP = {} #所有模块的name,Module对

def get_MODULE_MAP(key):
    if key in MODULE_MAP:
        return MODULE_MAP[key]

    return None

class DevControllers(http.Controller):

    @http.route('/dev/sankey.html', type='http', auth="public")
    def sankey_html(self, *args, **kw):
        return request.render('anodoo_develop_module.sankey')

    @http.route('/dev/sankey.json', type='http', auth='public', cors="*")
    def sankey_json(self,*args, **kw):

        c_type = request.httprequest.args.get('c_type', 2, type=int) #0,正常， 1 完整  2 简单


        c_only_prefix = request.httprequest.args.get('c_only_prefix', '') #值

        # 显示前缀的, 和c_only结合用
        c_only = set() #只显示其上层和下层的模块
        c_baseon = set() #只显示基于这些的模块

        c_only_arg = request.httprequest.args.get('c_only', '')
        c_baseon_arg = request.httprequest.args.get('c_baseon', '')
        if c_only_arg:
            c_only.update(c_only_arg.split(','))
        if c_baseon_arg:
            c_baseon.update(c_baseon_arg.split(','))


        env = request.env
        # 获取所有的module
        modules = env['ir.module.module'].search([], order="name")

        nodes = []
        links = []

        for module in modules:
            m = Module()
            m.name = module.name
            for d in module.dependencies_id:
                m.direct_source_set.add(d.name)

            MODULE_MAP[m.name] = m

        #所有间接依赖
        all_indirect_source_set()

        # c_only_prefix
        if c_only_prefix:
            for key in MODULE_MAP.keys():
                if key.startswith(c_only_prefix):
                    c_only.add(key)


        for key in MODULE_MAP.keys():
            module = get_MODULE_MAP(key)
            if key == 'mail':
                print('for debug')

            if module.name.startswith('l10n_'):
                continue
            if module.name.startswith('test_'):
                continue



            #c_only
            if len(c_only) > 0:
                all_dep = set()
                for only in c_only:
                    all_dep.update(get_MODULE_MAP(only).indirect_source_set)

                if module.name not in c_only and len(c_only.intersection(module.indirect_source_set)) == 0 and module.name not in all_dep:
                    continue

            #baseon 中没有他的基类，跳过
            if len(c_baseon) > 0:
                if module.name not in c_baseon and len(c_baseon.intersection(module.indirect_source_set)) == 0:
                    continue




            # if c_only_anodoo and not module.name.startswith('anodoo_'):
            #     continue
            setting = {
                "name":  module.name,
                "value": 1,
            }

            if module.name.startswith('anodoo_'):
                setting["depth"] = 15
                setting["itemStyle"] = {
                    "color":'#D9D919',
                    # "borderWidth": 3,
                    # "borderType": "dotted",
                }

            nodes.append(setting)

            dependencies = module.direct_source_set

            if c_type == 1:
                dependencies = module.indirect_source_set
            elif c_type == 2:
                module.simple()
                dependencies = module.simple_source_set

            for d in dependencies:
                links.append({
                  "source": d,
                  "target": module.name,
                  "value": 1
                })

        result = {
            "nodes": nodes,
            "links": links,
        }

        print('return json---------------')

        return request.make_response(
            data=json.dumps(result),
            headers=[('Content-Type', 'application/json')]
        )

def all_indirect_source_set():
    #所有间接依赖
    for module in MODULE_MAP.keys():
        one_indirect_source_set(MODULE_MAP[module])

#处理一个module的间接依赖
def one_indirect_source_set(module):
    if len(module.indirect_source_set) > 0:
        return;#如果已经处理过了，则不处理

    #将直接放入间接
    module.indirect_source_set.update(module.direct_source_set)

    #递归
    for s in module.direct_source_set:
        dep_module = get_MODULE_MAP(s)
        if dep_module:
            one_indirect_source_set(dep_module)
            module.indirect_source_set.update(dep_module.indirect_source_set)




class Module(object):

    def __init__(self):
        self.name = ''
        self.direct_source_set = set() #直接依赖
        self.indirect_source_set = set() #直接+间接依赖

        self.simple_source_set = set() #简化的直接依赖

    def simple(self):
        self.simple_source_set.update(self.direct_source_set)

        #如果依赖和直接依赖的依赖重复，则去掉
        for source in self.direct_source_set:
            for dep in self.direct_source_set:
                if source == dep:
                    continue

                dep_module = get_MODULE_MAP(dep)
                if dep_module:
                    if source in dep_module.indirect_source_set:
                        print(self.name + '的直接依赖在依赖' + dep + '的依赖中已经间接存在：' + source)
                        if source in self.simple_source_set:
                            self.simple_source_set.remove(source)
                            break

