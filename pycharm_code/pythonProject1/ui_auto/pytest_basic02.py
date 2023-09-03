# 测试类形式
class TestDemo(object):  # 正常定义类 测试类名必须以Test开头，否则执行无结果
    """测试示例类"""

    def test_method1(self):  # 正常定义方法 测试方法名必须以 test开头
        """测试方法1"""
        print('测试方法1')

    def test_method2(self):
        """测试方法2"""
        print('测试方法2')