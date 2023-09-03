"""
整合多个脚本至同一个测试用例中
尽力听 可以直接拿来用呜呜哈哈哈。。理解有难度的
运用utils 直接调用
"""
import pytest
from time import sleep
from selenium import webdriver

from V5.page_index import IndexTask
from V5.page_login import LoginTask
from utils import DriverUtil, get_alert_msg


class TestLogin(object):
    """登录测试类"""

    def setup_class(self):
        self.driver = DriverUtil.get_driver()  # 获取浏览器对象
        self.index_task = IndexTask()  # 实例化首页业务层兑对象
        self.login_task = LoginTask()  # 实例化登录页面业务层对象

    def teardown_class(self):
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setup(self):
        # 打开首页
        self.driver.get('http://novel.hctestedu.com/')
        # 点击登录
        self.index_task.go_to_login()  # 跳转登录

    def teardown(self):
        pass

    def test_account_does_not_exist(self):
        """账号不存在测试方法"""

        self.login_task.login_method('88890032513', '19980502')
        # 5.获取错误提示信息
        # 获取弹框信息
        msg = get_alert_msg()
        print("提示信息：", msg)

    def test_wrong_password(self):
        """密码错误"""

        # 执行登录
        self.login_task.login_method('13039131596', '123450')
        # 5.获取错误提示信息
        # 获取弹框信息
        msg = get_alert_msg()
        print("提示信息：", msg)


if __name__ == '__main__':
    pytest.main(['-s', 'test_Login.py'])
