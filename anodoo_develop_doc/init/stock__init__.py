
'''
odoo stock库存模块  非常关键的文章
https://blog.csdn.net/ieflex/article/details/100897610


Odoo 库存管理-库存移动（Stock Move）新玩法
http://www.mamicode.com/info-detail-1102946.html


stock_account	*	WMS会计	技术设置	TRUE	FALSE	stock , account , 
	stock_account_enterprise	*	企业股票账户	库存	TRUE	FALSE	stock_account , stock_enterprise , web_dashboard ,
	sale_stock
	purchase_stock
	stock_intrastat	*	库存Intrastat	库存	TRUE	FALSE	stock_account , account_intrastat , 

stock_barcode	*	条码	库存	FALSE	TRUE	barcodes , stock , web_tour , 
	stock_barcode_mobile	*	移动设备中的库存条码	手机	TRUE	FALSE	stock_barcode , web_mobile , 
	stock_barcode_quality_control	*	条码质检模块	技术设置	TRUE	FALSE	stock_barcode , quality_control , 
stock_dropshipping	*	直销	库存	FALSE	FALSE	sale_purchase , sale_stock , purchase_stock , 
stock_enterprise	*	库存企业	库存	TRUE	FALSE	stock , web_dashboard , web_cohort , web_map , web_grid , 

stock_landed_costs	*	WMS到岸成本	库存	FALSE	FALSE	stock_account , purchase_stock , 
stock_picking_batch	*	仓库管理：批量调拨	库存	FALSE	FALSE	stock , 
stock_sms	*	库存 - 短信	技术设置	TRUE	FALSE	stock , sms , 


实体

stock.warehouse  仓库
    仓库和位置的关系通过在仓库中设置

stock.location  仓库内的位置区域，是树状结构
    usage：类型，有层级用途的view;客户，供应商不是按不同公司设置的？
stock.location.route  路线

 stock.rule规则， 一个路线下是多个规则
procurement.group 采购组，用来将多个产品一起采购

stock.picking
stock.picking.type  每一个仓库，都有不同的调拨类型
stock.picking.batch  批量调拨

stock.move  一个调拨单有多个产品的move单，也就是作业
stock.move.line  详细作业，一个作业可以对应多个详细的实际的作业



stock.warehouse.orderpoint 订货规则，安全库存，最小订货触发

product.packaging

stock.quant  代表了一定数量的某个产品，用来计算在手数量
stock.quant.package  邮包， 一个包裹下有多个quant




stock.production.lot  序列号，定义是简单的，主要是如何使用它。
    一个产品有多个批号，外购产品也有序列号，可能和外部的不一样
stock.scrap  报废  一个报废会关联一个stock.move

stock.inventory 盘点
stock.inventory.line 一个盘点内的明细

stock.package_level 一次调拨，一个包裹内的 move_ids的状态，在计算atp时使用

product.removal  下架策略， 先进先出等。 产品类型，产品位置中设置
stock.putaway.rule  上架规则，产品到了某一个区域，自动到下级区域

位置类型
"* Vendor Location: Virtual location representing the source location for products coming from your vendors"
             "\n* View: Virtual location used to create a hierarchical structures for your warehouse, aggregating its child locations ; can't directly contain products"
             "\n* Internal Location: Physical locations inside your own warehouses,"
             "\n* Customer Location: Virtual location representing the destination location for products sent to your customers"
             "\n* Inventory Loss: Virtual location serving as counterpart for inventory operations used to correct stock levels (Physical inventories)"
             "\n* Production: Virtual counterpart location for production operations: this location consumes the components and produces finished products"
             "\n* Transit Location: Counterpart location that should be used in inter-company or inter-warehouses operations")

'''


调度器
stock.ir_cron_scheduler_action
    调用procurement.group的方法：run_scheduler

路线和规则，路线下有几个规则