继承mrp，没有子模块

扩展
mrp.bom  增加版本
mrp.bom.line


mrp.eco.approval.template
mrp.eco.approval

mrp.eco.type
    is_blocking（是否阶段被审批人阻塞了）， allow_apply_change  final_stage  approval_template_ids
mrp.eco.stage
mrp.eco.tag

mrp.eco
mrp.eco.bom.change  bom物料变更记录和明细
mrp.eco.routing.change  工序bom物料变更记录和明细


eco状态
state = fields.Selection([   这个是bom变更的状态。 eco.stage是变更流程的阶段。二者是有区别的。
        ('confirmed', 'To Do'),  默认
        ('progress', 'In Progress'),  开始编辑bom结构了
        ('rebase', 'Rebase'),
        ('conflict', 'Conflict'),  冲突了
        ('done', 'Done')], string='Status',  应用了变更
        copy=False, default='confirmed', readonly=True, required=True)

types = [  还有'routing', 'both'
            ('product', _('Product Only')),
            ('bom', _('Bill of Materials'))]


ECO， 包括mrp.eco， tag，stage，以及bom的变更记录，routing变更记录

审批如何实现？
ECO 即工程更改定单(Engineering Change Order)，在MRPII系统中用于定义和修改清单，使清单的修改过程有可追溯性。为控制某些清单定义或更改能同时生效，每个ECO可以同时定义或更改多份清单，例如在多份清单中替换某个部件，或定义同一产品的几份清单。