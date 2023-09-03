"""
    目标：unittest框架--TestCase使用
    步骤：
        1.导包
        2.新建类并继承unittest.TestCase
        3.测试方法必须以test字母开头
"""
#导包
import unittest

#编写求和函数
def add(x,y):
    return x+y

#定义测试类并继承
class Test01(unittest.TestCase):
    def test_add(self):
        result=add(1,2)
        print("结果为：",result)

    def test_add2(self):
        result=add(122,2)
        print("结果为：",result)









