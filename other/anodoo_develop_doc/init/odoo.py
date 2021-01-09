#!/usr/bin/env python3

# set server timezone in UTC before time module imported
__import__('os').environ['TZ'] = 'UTC'
import odoo

if __name__ == "__main__":
    odoo.cli.main()



# L5: Import odoo就会引起很多函数被调用
# 	n 将odoo下的__init__执行，并创建其中的变量
# 	n 引入odoo下的所有py文件，创建为对应的module对象
# 	n 级联引入所有的module对象
# l  
# L8: 调用odoo.cli.main()
# 参考cli的main()函数