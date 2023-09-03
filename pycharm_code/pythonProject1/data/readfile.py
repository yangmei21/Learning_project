from data.test_login import TestLogin
from excel_reader import excelread

"""
如何想文本文档里获取值
简单的数据分离--数据驱动思想
同样的思想可以有不同的载体，换一个清晰的东西
"""

# 此方法是读txt文件方式：
# file = open(r'F:\IDE test文件\account.txt')
# name = file.readline()
# password = file.readline()  # 一行一行读
# TestLogin().test_login(name, password)

"""
能读Excel的东西
"""
lst=excelread().read()
for ls in lst:
    name=ls[0]
    password=ls[1]
    TestLogin().test_login(name,password)
    from time import sleep
    sleep(3)