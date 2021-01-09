


documents.document  包含附件ir.attachment
documents.mixin
documents.folder
documents.share
documents.facet  the facets (tag categories)
documents.tag  每一个类别下的tag是互斥的，多选一


documents.workflow.rule  继承这个，定义新的create_model
    实现针对文档进行自动化操作
documents.workflow.action 这个是针对tag的add，remove，replace


相关模块
更多的是实现模块业务对象和文档的关联，以及根据文档创建特定模块下的业务对象，定义新的create_model


mixin的使用方法参考如下
class HrEmployee(models.Model):
    _name = 'hr.employee'
    _inherit = ['hr.employee', 'documents.mixin']

    def _get_document_folder(self):
        return self.company_id.documents_hr_folder

    def _get_document_owner(self):
        return self.user_id

    def _check_create_documents(self):
        return self.company_id.documents_hr_settings and super()._check_create_documents()
