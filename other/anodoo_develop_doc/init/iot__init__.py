
iotbox上安装nginx
iotbox会连接server
iotbox会自动向server更新device

实体
iot.box  每一个box都有一个ip，ip_url，box里面的image都有不同的版本，或许要装驱动



odoo的业务模块怎么实现从iotbox中获取数据
message_post？这个是发送数据吧
bus.bus

模块
以下模块installable = False，用于iot box

hw_drivers
    Hardware Poxy
    =============

    This module allows you to remotely use peripherals connected to this server.

    This modules only contains the enabling framework. The actual devices drivers
    are found in other modules that must be installed separately.
hw_escpos
    ESC/POS©指令体系是由EPSON发明的一套专有POS打印机指令系统
    市面上绝大部分打印机兼容esc/pos指令。
hw_posbox_homepage
    页面功能，依赖hw_drivers


企业版
load_certificate 函数访问官方


delivery_iot