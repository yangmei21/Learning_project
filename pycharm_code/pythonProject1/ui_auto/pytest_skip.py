"""
跳过功能
"""
import pytest

version = 25  # 模拟软件版本号变量


class TestDemo(object):
    def test_method1(self):
        print('test1')

    # 语法：@pytest.mark.skipif(符合的条件，reason=‘跳过的原因’)
    # 注意：reason=不能省略，否则报错！
    # @pytest.mark.skipif(version>=25,'***')--错误样例
    @pytest.mark.skipif(version >= 25, reason='***')
    def test_method2(self):
        print('test2')

    def test_method3(self):
        print('test3')


if __name__ == '__main__':
    pytest.main(['-s', 'pytest_skip.py'])
