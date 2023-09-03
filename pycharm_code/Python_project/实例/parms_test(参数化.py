import unittest

"""
    目标：parameterized插件应用
    步骤：
        1.导包from parameterized import parameterized
        2.修饰测试函数@parmeterized.expand(列表类型数据)
        3.在测试函数中使用变量接收，传递过来的值
        
    语法：
        1.单个参数：值为列表
        2.多个参数：值为列表嵌套元组 如：[(1,2,3),(2,3,5)]
"""

import unittest
from parameterized import parameterized

def add(x,y):
    return x+y

def get_data():
    return[(1,2,3),(5,6,11),(3,7,10)]

class Test01(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_add(self,a,b,expect):
        result=add(a,b)
        assert  result==expect




