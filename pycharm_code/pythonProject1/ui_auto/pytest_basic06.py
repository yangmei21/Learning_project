"""
特殊方法：函数级别
"""
import pytest


class TestDemo(object):
    """测试示例类"""

    def setup_class(self):
        """开始方法"""
        print('类-》开始')

    def teardown_class(self):
        """结束方法"""
        print('类-》结束')

    def test_method(self):
        """测试示例类"""
        print('测试方法')


if __name__ == '__main__':
    pytest.main(['-s', 'pytest_basic06.py'])
