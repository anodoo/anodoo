cd ~/odoo-dev/anodoo

(将process批量替换为新模块)

mkdir anodoo_process;
\cp -r -a ../custom-addons/siwei_module_template/* anodoo_process;   

mv anodoo_process/controllers/oppor_controllers.py anodoo_process/controllers/process_controllers.py;
mv anodoo_process/data/oppor_data.xml anodoo_process/data/process_data.xml;
mv anodoo_process/demo/oppor_demo.xml anodoo_process/demo/process_demo.xml;
mv anodoo_process/models/oppor_models.py anodoo_process/models/process_models.py;
mv anodoo_process/security/oppor_security.xml anodoo_process/security/process_security.xml;
mv anodoo_process/views/oppor_menu.xml anodoo_process/views/process_menu.xml;
mv anodoo_process/views/oppor_templates.xml anodoo_process/views/process_templates.xml;
mv anodoo_process/views/oppor_views.xml anodoo_process/views/process_views.xml;

进入eclipse, 刷新, 选择模块, 在当前resource中, 批量替换oppor 为 process  应该有9个地方
修改mani文件

