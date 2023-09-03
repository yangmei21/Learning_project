"""
    目标：unittest框架 TestSuite使用
    操作
     1.导包
     2.实例化获取TestSuite对象
     3.调用addTest方法添加用例到指定套件中
"""

#导包
import unittest
from 实例.testcase使用 import Test01

#实例化suite
suite=unittest.TestSuite()
#调用添加方法
#写法1 类名("方法名")  注意：方法名称使用双引号
suite.addTest(Test01("test_add"))

#扩展 添加测试类中所有test开头的方法
suite.addTest(unittest.makeSuite(Test01))

#执行测试套件
runner=unittest.TextTestRunner()
runner.run(suite)







