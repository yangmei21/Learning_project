"""
    目标：演示TestLoader（）类的用法
    作用：搜索指定目录下指定开头的py文件，在py文件中搜索test开头测试方法，并且将这些方法添加到测试套件中
    需求：
        运行cases目录下test01.py-test02.py文件
    操作：
        1.导包unittest
        2.调用TestLoader类下discaver方法
        3.执行测试用例
"""

#导包
import unittest
#1----调用方法
#suite=unittest.TestLoader().discover("../case")

#2----扩展 指定tpshop开头的模块
#suite=unittest.TestLoader().discover("../case",pattern="tpshop*.py")

#3----扩展 使用
suite=unittest.defaultTestLoader.discover("../case")

#执行套件方法texttestrunner
unittest.TextTestRunner().run(suite)











