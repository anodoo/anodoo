

MRP(Material Requirement Planning 物料需求bai计划)是被设计并用于制造业库存du管理信zhi息处理的系统，它解决了如dao何实现制造业库存管理目标——在正确的时间按正确的数量得到所需的物料这一难题。

制造资源计划MRPⅡ（ManufacturingResourcePlanning）是以生产计划为中心，把与物料管理有关的产、供、销、财各个环节的活动有机地联系起来，形成一个整体，进行协调，使它们在生产经营管理中发挥最大的作用。其最终的目标是使生产保持连续均衡，最大限度地降低库存与资金的消耗，减少浪费，提高经济效益。从MRP发展到MRPⅡ，是对生产经营管理过程的本质认识不断深入的结果，体现了先进的计算机技术与管理思想的不断融合，因此MRP发展为MRPⅡ是一个必然的过程。

企业资源计划ERP（EnterpriseResourcePlanning）是从制造资源计划MRPⅡ发展而来的新一代集成化企业资源管理系统，它扩展了MRPⅡ功能。ERP对MRPⅡ的扩展朝三个方向延伸：横向的扩展――功能范围的增加，从供应链上游的供应商管理到下游的客户关第管理；纵向的扩展――从低层的数据处理（手工自动化）到高层管理决策支持（职能化管理）；行业的扩展――从传统的以制造业为主到面向所有的行业。总结起来说，MRP→MRP II→ERP是一脉相承的发展过程，是对制造业的信息化管理的一个不断深化的过程。


继承自stock，生产和库存的关系密切。

BOM
mrp.bom
mrp.bom.line
mrp.bom.byproduct 副产品

mrp.document  文档，就是ir.attachment
    查看文档的action是动态的，

mrp.production 生产订单
mrp.unbuild 拆解

mrp.workcenter.productivity  一个生产订单，工单在某一个工作中心的具体的生产？
mrp.workcenter.productivity.loss  阻塞的原因（生产力损失）  select * from mrp_workcenter_productivity_loss
mrp.workcenter.productivity.loss.type




工单
mrp.workcenter
mrp.workorder 生产工单


MPS
生产计划，销售计划的连接。自动创建采购，生成单据
可设置公司的生产计划是按周，月等，可显示哪些字段

mrp.production.schedule  MPS是指主生产计划（Master Production Schedule，简称MPS）  针对一个产品的预测
mrp.product.forecast

生成与库存

会创建一个('mrp_operation', 'Manufacturing')的调拨类型stock.picking.type，可以理解为领料，入库等
库存不足，通过生产补货时候，入库单关联生产单等
规则stock.rule中也会增加('manufacture', 'Manufacture')
在生产工单中报废


mrp.routing.workcenter
工序，必然属于某一个bom里面，（没法创建公共工序，是否是问题？）

