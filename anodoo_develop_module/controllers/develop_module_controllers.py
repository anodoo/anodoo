# -*- coding: utf-8 -*-

from odoo import http

from odoo import http
from odoo.http import request

import datetime
import os


class DevelopControllers(http.Controller):

    #创建模块列表，到处为csv文件
    @http.route('/dev/modulelist', type='http', auth="user")
    def module_list(self, anodoo=False, *args, **kw):
        now = datetime.datetime.now()
        posfex = now.strftime('%Y%m%d%H%M%S')  # '%Y-%m-%d %H:%M:%S'

        file_path = '/home/lionger/Temp/module_list_' + posfex + '.csv'

        print(file_path)
        file = open(file_path, 'a')

        env = request.env
        # 获取所有的module
        Module = env['ir.module.module']
        modules = Module.search([], order="name")

        str_content = ''
        for module in modules:
            str_content += '"' + str(module.name) + '",'
            str_content += '"' + str(module.shortdesc) + '",'
            str_content += '"' + str(module.category_id.name) + '",'
            # str_content += '"' + module.description + '",'
            str_content += '"' + str(module.website) + '",'
            str_content += '"' + str(module.auto_install) + '",'
            str_content += '"' + str(module.application) + '",'
            # str_content += '"' + module.menus_by_module + '",'
            # str_content += '"' + module.reports_by_module + '",'
            # str_content += '"' + module.views_by_module + '",'

            str_d = ''
            for d in module.dependencies_id:
                str_d += d.name + '|'

            str_content += '"' + str_d + '"'

            str_content += '\n'

        file.write(str_content)

        file.close()

        print('make module list finished')


    #生成每一个模块的info文件
    @http.route('/dev/moduleinfo', type='http', auth="user")
    def module_info(self, anodoo=False, *args, **kw):
        # https://jingyan.baidu.com/article/5970355293c2508fc107407b.html
        now = datetime.datetime.now()
        posfex = now.strftime('%Y%m%d%H%M%S')  # '%Y-%m-%d %H:%M:%S'

        dir_path = '/home/lionger/Temp/module_info_' + posfex

        print(dir_path)
        os.mkdir(dir_path)

        env = request.env
        # 获取所有的module
        Module = env['ir.module.module']
        modules = Module.search([])
        for module in modules:
            if anodoo and not module.name.startswith('anodoo_'):
                continue

                # https://www.runoob.com/python/file-methods.html
            file_path = dir_path + '/x' + module.name + '.txt'
            file = open(file_path, 'a')

            self._make_module_info(env, file, module)

            file.close()

        print('make module info finished')


    def _make_module_info(self, env, file, module):
        str_content = '模块:' + module.name + '       ID:' + str(module.id) + '      Name:' + module.shortdesc + '\n'

        str_content += self._make_model_info(env, module)

        file.write(str_content)


    def _make_model_info(self, env, module):
        Model = env['ir.model']
        models = Model.search(['|', ('modules', '=', module.name), ('modules', '=like', module.name + ",%")])

        str_content = ''
        str_content += '\n\n' + '================== Models ======================' + '\n'
        for model in models:
            str_content += '\n###' + model.model + ' name:' + model.name + ' inherit:' + str(model.inherited_model_ids) + \
                           '  access:' + str(model.access_ids) + '  rule:' + str(model.rule_ids) + '  transient:' + str(
                model.transient) + '  modules:' + model.modules \
                           + '\n'

        str_content += '\n\n' + '================== Extended Models ======================' + '\n'
        extend_models = Model.search(
            ['|', ('modules', 'like', ', ' + module.name + ','), ('modules', '=like', '%, ' + module.name + '')])
        for extend_model in extend_models:
            str_content += '\n###' + extend_model.model + ' name:' + extend_model.name + ' inherit:' + str(
                extend_model.inherited_model_ids) + \
                           '  transient:' + str(extend_model.transient) + '  modules:' + extend_model.modules \
                           + '\n'

        ActWindow = env['ir.actions.act_window']
        str_content += '\n\n' + '================== Actions ======================' + '\n'
        for model in models:
            actions = ActWindow.search([('res_model', '=', model.model), ('type', '=', 'ir.actions.act_window')])
            for action in actions:
                str_content += '\n###' + action.xml_id + '  name:' + action.name + ' view_mode:' + action.view_mode + ' domain:' + str(
                    action.domain) + \
                               '  context:' + str(action.context) \
                               + '\n'

        str_content += '\n\n' + '================== Views ======================' + '\n'
        for model in models:
            str_content += '\n\n###' + model.model + ' \n'
            for view in model.view_ids:
                str_content += '\n' + view.xml_id + '  type:' + view.type + '  priority:' + str(
                    view.priority) + '  arch_fs:' + view.arch_fs + '  inherit_id:' + str(
                    view.inherit_id.xml_id if view.inherit_id else '') + '\n'

        str_content += '\n\n' + '================== Extended Views ======================' + '\n'
        for extend_model in extend_models:
            str_content += '\n\n###' + extend_model.model + ' \n'
            for view in extend_model.view_ids:
                if not view.xml_id.startswith(module.name):
                    continue

                str_content += '\n' + view.xml_id + '  type:' + view.type + '  priority:' + str(
                    view.priority) + '  arch_fs:' + view.arch_fs + '  inherit_id:' + str(
                    view.inherit_id.xml_id if view.inherit_id else '') + '\n'

        str_content += '\n\n' + '================== qWeb ======================' + '\n'
        QWeb = env['ir.ui.view']
        qwebs = QWeb.search([('key', 'like', module.name + '.%'), ('type', '=', 'qweb')])
        for qweb in qwebs:
            str_content += '\n' + str(qweb.key) + '  type:' + qweb.type + '  priority:' + str(
                qweb.priority) + '  arch_fs:' + str(qweb.arch_fs) + '  inherit_id:' + str(
                qweb.inherit_id.xml_id if qweb.inherit_id else '') + '\n'

        str_content += '\n\n' + '================== Fields ======================' + '\n'
        for model in models:
            str_content += '\n\n###' + model.model + ' \n'
            for field in model.field_id:
                relation = 'relation:' + field.relation + '  ' if field.relation else ''
                str_content += '\n' + field.name + ' Label:' + str(
                    field.field_description) + '  ttype:' + field.ttype + "  " + relation + '  required:' + str(
                    field.required) + '  compute:' + str(field.compute) + '  depends:' + str(
                    field.depends) + '  modules:' + field.modules + '  help:' + str(field.help)

        str_content += '\n\n' + '================== Extended Fields ======================' + '\n'
        for extend_model in extend_models:
            str_content += '\n\n###' + extend_model.model + ' \n'
            for field in extend_model.field_id:
                if field.modules == module.name or field.modules.startswith(module.name + ','):
                    relation = 'relation:' + field.relation + '  ' if field.relation else ''
                    str_content += '\n' + field.name + ' Label:' + str(
                        field.field_description) + '  ttype:' + field.ttype + "  " + relation + '  required:' + str(
                        field.required) + '  compute:' + str(field.compute) + '  depends:' + str(
                        field.depends) + '  modules:' + field.modules + '  help:' + str(field.help)

        return str_content
