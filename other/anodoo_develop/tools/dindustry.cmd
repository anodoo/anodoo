cd ~/odoo-dev/anodoo

(将demo批量替换为新模块)

mkdir industry_auto4s;
\cp -r -a ../custom-addons/siwei_module_template/* industry_auto4s;   

mv industry_auto4s/controllers/oppor_controllers.py industry_auto4s/controllers/auto4s_controllers.py;
mv industry_auto4s/data/oppor_data.xml industry_auto4s/data/auto4s_data.xml;
mv industry_auto4s/demo/oppor_demo.xml industry_auto4s/demo/auto4s_demo.xml;
mv industry_auto4s/models/oppor_models.py industry_auto4s/models/auto4s_models.py;
mv industry_auto4s/security/oppor_security.xml industry_auto4s/security/auto4s_security.xml;
mv industry_auto4s/views/oppor_menu.xml industry_auto4s/views/auto4s_menu.xml;
mv industry_auto4s/views/oppor_templates.xml industry_auto4s/views/auto4s_templates.xml;
mv industry_auto4s/views/oppor_views.xml industry_auto4s/views/auto4s_views.xml;

进入eclipse, 刷新, 选择模块, 在当前resource中, 批量替换oppor 为 auto4s  应该有9个地方
修改mani文件

