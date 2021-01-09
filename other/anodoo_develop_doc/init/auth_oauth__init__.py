# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models

'''

l Github
	n https://blog.csdn.net/weixin_41126141/article/details/81675740
	n https://blog.csdn.net/suprezheng/article/details/85298011
		u 
l 微信
	n https://blog.csdn.net/qq_35556064/article/details/81637193
l 钉钉
	n https://baijiahao.baidu.com/s?id=1596175378719005273&wfr=spider&for=pc
	n https://www.cnblogs.com/zhou-tt/p/11417472.html
l QQ
	n https://wiki.open.qq.com/wiki/【QQ登录】网站接入#2.1_.E6.8F.90.E4.BA.A4.E6.8E.A5.E5.85.A5.E7.94.B3.E8.AF.B7
	n https://www.cnblogs.com/wuxl360/p/5454272.html
 
 
https://www.odoo.com/apps/modules/10.0/oauth_signup/  4个国外的google,facebook,twitter,linkedin的
https://www.odoo.com/apps/modules/12.0/auth_oauth_dingtalk/  dingding 山西清水欧读
 
 
 
 
访问/web/web_login ,进入修改后的login页面.点击第三方,进入他们的链接.登陆后返回auth_oauth/signin.
调用auth_oauth中的res_users的auth_oauth方法
	验证access_token
	根据之前的登陆信息,如果对上,直接登陆
	没对上,根据no_user_creation决定是否创建一个(后续应该是可关联)
 
扩展点:_auth_oauth_signin
 
odoo账号登录
https://accounts.odoo.com/oauth2/auth?response_type=token&client_id=2667ec8c-3140-11ea-b14e-a44e31ce7b70&redirect_uri=http%3A%2F%2Flocalhost%3A8070%2Fauth_oauth%2Fsignin&scope=userinfo&state=%7B%22d%22%3A+%22lionger%22%2C+%22p%22%3A+1%2C+%22r%22%3A+%22http%253A%252F%252Flocalhost%253A8070%252Fweb%22%7D
返回
dict: {'d': 'lionger', 'p': 1, 'r': 'http%3A%2F%2Flocalhost%3A8070%2Fweb'}
c  context
 
githbub登录
文档:https://developer.github.com/apps/about-apps/ 
0 users
 
Client ID
03fe6a5003a436f9474a
Client Secret
0bc81539e24973876f8f98e058ff756354f603eb
 
https://github.com/login/oauth/authorize?response_type=token&client_id=03fe6a5003a436f9474a&redirect_uri=http%3A%2F%2Flocalhost%3A8070%2Fauth_oauth%2Fsignin&scope=False
&state=%7B%22d%22%3A+%22lionger%22%2C+%22p%22%3A+4%2C+%22r%22%3A+%22http%253A%252F%252Flocalhost%253A8070%252Fweb%22%7D
转为
https://github.com/login?client_id=03fe6a5003a436f9474a&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D03fe6a5003a436f9474a%26redirect_uri%3Dhttp%253A%252F%252Flocalhost%253A8070%252Fauth_oauth%252Fsignin%26response_type%3Dtoken%26scope%3DFalse%26state%3D%257B%2522d%2522%253A%2B%2522lionger%2522%252C%2B%2522p%2522%253A%2B4%252C%2B%2522r%2522%253A%2B%2522http%25253A%25252F%25252Flocalhost%25253A8070%25252Fweb%2522%257D
 
 
talkding登录
#state 没有用
return_url 为什么自定义
 
 
登陆记录
 
参考hr_presence 
  @route('/longpolling/poll', type="json", auth="public")
    def poll(self, channels, last, options=None):
 
登陆流程
	res_users.  authenticate(cls, db, login, password, user_agent_env):
	调用_login, 里面更新最后登陆记录 user._update_last_login()
 
web website 分别都有web_login方法  还有其他继承了web_login, 如AuthSignupHome, OAuthLogin
修改登陆界面 : web.webclient_templates.xml  auth_signup  auth_signup_login_templates.xml
	auth_signup.signup, uth_signup.reset_password 注入到web.login_layout
	auth_signup.login 继承 web.login  web.login注入到web.login_layout
	web.login_layout 注入到web.frontend_layout
	web.frontend_layout 继承 web.layout(这个是根本)
	web.layout  : 搜索:<template id="web.layout" name="Web layout">
 
	portal.frontend_layout 继承 web.frontend_layout
	website.layout(<template id="layout") 继承portal.frontend_layout
	website.login_layout 继承web.login_layout,将其主体改为website.layout
 
 
style="background-image: url('/anodoo_base/static/src/img/background_login_1.png')"
 
<t t-set="x_icon" t-value="website.image_url(website, 'favicon')"/>
 
 &quot; style=&quot;background-image: url('/anodoo_base/static/src/img/background_login_1.png')&quot;

'''
