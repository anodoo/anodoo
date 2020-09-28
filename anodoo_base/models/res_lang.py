# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools

class Lang(models.Model):
    _inherit = 'res.lang'

    #去掉，手动操作
    #Override 如果未设置load_language,则默认改为中文,如果设置了,则按照设置
    @api.model
    def install_lang_zh(self):
        load_language = tools.config.get('load_language')
        if not load_language:
        
            lang_code = 'zh_CN'
            lang = self._lang_get(lang_code)
            if not lang:
                self.load_lang(lang_code)
            
            #partner默认为中文    
            IrDefault = self.env['ir.default']
            IrDefault.set('res.partner', 'lang', lang_code)
                
            #公司为中文
            partner = self.env.company.partner_id
            partner.write({'lang': lang_code})
            
            admin = self.env.ref('base.partner_admin')
            admin.write({'lang': lang_code})
            
            root = self.env.ref('base.partner_root')
            root.write({'lang': lang_code})
            
        return True
        