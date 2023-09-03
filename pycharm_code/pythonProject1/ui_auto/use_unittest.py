"""
使用TestCase
"""
import unittest

class TestDemo(unittest.TestCase):
    """自定义测试类"""
    def test_method1(self):
        print("测试方法1")

    def test_method2(self):
        print("测试方法2")


if __name__=='__main__':
    unittest.main()