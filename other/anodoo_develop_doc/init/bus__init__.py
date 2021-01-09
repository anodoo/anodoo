"Instant Messaging Bus allow you to send messages to users, in live.",

'''

bus
	系统内发送消息,res.partner, res.users 的IM状态
	表:bus_presence
	select * from bus_bus  发送消息
select * from bus_presence  记录在线状态

IM Bus
在线聊天,类似qq,系统内

	依赖
	Base,web
	实体
	Bus.bus(ImBus)
	Bus.presence
	扩展
	Partner,user的im在线状态
	分发器
	ImDispatch,应该有一个线程或端口
	轮询longpolling


select * from bus_bus;
select * from bus_presence;


发送消息：def sendone(self, channel, message):
channel  ["dev2","res.partner",3]
message   {"type":"message_notification_update","elements":[{"id":488,"res_id":35,"model":"stock.picking","res_model_name":"\u8f6c\u8d26","date":"2020-12-03 08:05:27","message_type":"notification","notifications":[{"id":45,"notification_type":"email","notification_status":"exception","failure_type":"SMTP","res_partner_id":[14,"Azure Interior"]}]}]}
'''
