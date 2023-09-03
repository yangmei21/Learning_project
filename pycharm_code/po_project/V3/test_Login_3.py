"""
整合多个脚本至同一个测试用例中
尽力听 可以直接拿来用呜呜哈哈哈。。理解有难度的
运用utils 直接调用
"""
import pytest
from time import sleep
from selenium import webdriver

from utils import DriverUtil, get_alert_msg


class TestLogin(object):
    """登录测试类"""

    def setup_class(self):
        # self.driver = webdriver.Chrome()
        # self.driver.get('http://novel.hctestedu.com/')
        # self.driver.maximize_window()  # 窗口最大化
        # self.driver.implicitly_wait(10)  # 隐式等待
        self.driver = DriverUtil.get_driver()  # 获取浏览器对象

    def teardown_class(self):
        # sleep(2)
        # self.driver.quit()
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setup(self):
        # self.driver = webdriver.Chrome()
        # self.driver.get('http://novel.hctestedu.com/')
        # self.driver.maximize_window()  # 窗口最大化
        # self.driver.implicitly_wait(10)  # 隐式等待
        # 打开首页
        self.driver.get('http://novel.hctestedu.com/')
        # 点击登录
        self.driver.find_element_by_partial_link_text("登录").click()

    def teardown(self):
        # sleep(1)
        # self.driver.quit()
        pass

    def test_account_does_not_exist(self):
        """账号不存在测试方法"""

        # 2.输入一个不存在的用户名
        self.driver.find_element_by_id("txtUName").send_keys("88890032513")
        # 3.输入密码
        self.driver.find_element_by_id("txtPassword").send_keys("19980502")
        # 4.点击登录按钮
        self.driver.find_element_by_id("btnLogin").click()
        # 5.获取错误提示信息
        # sleep(2)
        # msg = self.driver.find_element_by_id("LabErr").text
        # # 断言
        # 获取弹框信息
        msg = get_alert_msg()
        print("提示信息：", msg)

    def test_wrong_password(self):
        """密码错误"""

        # 2.输入用户名
        self.driver.find_element_by_id("txtUName").send_keys("13039131596")
        # 3.输入错误密码
        self.driver.find_element_by_id("txtPassword").send_keys("123450")
        # 4.点击登录按钮
        self.driver.find_element_by_id("btnLogin").click()
        # 5.获取错误提示信息
        # sleep(2)
        # msg = self.driver.find_element_by_id("LabErr").text
        # 断言
        # print("提示信息：", msg)
        # 获取弹框信息
        msg = get_alert_msg()
        print("提示信息：", msg)


if __name__ == '__main__':
    pytest.main(['-s', 'test_Login.py'])
