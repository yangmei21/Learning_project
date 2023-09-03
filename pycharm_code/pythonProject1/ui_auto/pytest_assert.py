"""
pytest断言
"""
import pytest


def add_func(num1, num2):
    # 加法函数
    return num1 + num2


class TestDemo(object):
    """示例测试类"""

    def test_method(self):
        """加法测试方法"""
        # 调用被测函数
        result = add_func(1, 2)
        # 断言判断结果
        assert 3 == result


if __name__ == '__main__':
    pytest.main(['-s', 'pytest_assert.py'])
