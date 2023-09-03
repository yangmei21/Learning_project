"""
pytest参数化：通过方法引入数据
"""
import pytest


def build_test_data():
    """构造测试数据函数"""
    # 中间代码略
    return [('admin001', 123456), ('test001', 999333)]


class TestDemo(object):
    """示例测试类"""

    @pytest.mark.parametrize('name,pwd', build_test_data())
    def test_method(self, name, pwd):
        """测试方法"""
        print('账号：{} 密码：{}'.format(name, pwd))


if __name__ == '__main__':
    pytest.main(['-s', 'pytest_para2.py'])
