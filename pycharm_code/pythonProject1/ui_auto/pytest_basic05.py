"""
特殊方法：函数级别
"""
import pytest


class TestDemo(object):
    """测试示例类"""

    def setup(self):
        """开始方法"""
        print('函数-》开始')

    def teardown(self):
        """结束方法"""
        print('函数-》结束')

    def test_method(self):
        """测试示例类"""
        print('测试方法')


if __name__ == '__main__':
    pytest.main(['-s', 'pytest_basic05.py'])
