"""
控制方法执行顺序插件
"""
import pytest


class TestDemo(object):
    # 语法：@pytest.mark.run(order=序号)
    # 注意：run(order=序号)没有代码提示，需要手写
    @pytest.mark.run(order=3)
    def test_method1(self):
        print('测试方法1')

    @pytest.mark.run(order=2)
    def test_method2(self):
        print('测试方法2')

    @pytest.mark.run(order=1)
    def test_method3(self):
        print('测试方法3')

# 扩展：序号支持正数、负数，正负混合
# 纯正数：数越小，优先级越高
# 纯负数：数越小，优先级越高
# 正负混合：正数先按照顺序执行，负数最后执行
