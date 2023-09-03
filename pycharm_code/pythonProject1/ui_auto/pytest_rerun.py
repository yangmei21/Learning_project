"""
pytest失败重试插件
"""

class TestDemo(object):
    """示例测试类"""

    def test_method1(self):
        """测试方法"""
        print(1/0)