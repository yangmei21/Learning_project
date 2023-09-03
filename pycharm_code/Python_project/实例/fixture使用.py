"""
    目标：unittest中的fixture用法
    fixture其实就是两个函数，这个函数可以一起使用，也可以单独使用
        1.初始化函数： def setUp()
        2.结束函数：   def tearDowm
"""
import unittest

class Test03(unittest.TestCase):
    def setUp(self):
        print("setUp被执行")

    def tearDown(self):
        print("tearDown被运行")

    def test01(self):
        print("test01被执行")

    def test02(self):
        print("test02被执行")