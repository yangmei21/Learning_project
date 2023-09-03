# 测试函数形式
import pytest


def test_func():  # 要求函数名以test开头
    """测试函数"""
    print('我是测试函数')


if __name__ == '__main__':
    # pytest.main(['-s','文件名'])
    pytest.main(['-s', 'pytest_basic03.py'])
