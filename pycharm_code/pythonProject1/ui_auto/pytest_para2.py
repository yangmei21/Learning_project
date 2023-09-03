"""
pytest参数化：多个参数
"""
import pytest


class TestDemo(object):
    """示例测试类"""

    # 语法：@pytest.mark.parametrize('参数1,参数n',[(数据1-1，数据1-2),(数据2-1，数据2-2),...])
    # 注意：
    # 1.多个参数必须置于同一个字符串之内
    # 2.数据格式必须是：[(),()]或者[[],[]]
    # 扩展：另一种写法
    @pytest.mark.parametrize('name,pwd', [('admin001', 123456), ('test001', 999333)])
    def test_method(self, name, pwd):
        """测试方法"""
        print('账号：{} 密码：{}'.format(name, pwd))


if __name__ == '__main__':
    pytest.main(['-s', 'pytest_para2.py'])
