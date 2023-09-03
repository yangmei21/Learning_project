"""
整合多个脚本至同一个测试用例中
"""
import pytest
from time import sleep
from selenium import webdriver


class TestLogin(object):
    """登录测试类"""

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://novel.hctestedu.com/')
        self.driver.maximize_window()  # 窗口最大化
        self.driver.implicitly_wait(10)  # 隐式等待

    def teardown_class(self):
        sleep(1)
        self.driver.quit()

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

        # 1.点击首页的”登录“链接，进入登录页面
        # self.driver.find_element_by_partial_link_text("登录").click()
        # 2.输入一个不存在的用户名
        self.driver.find_element_by_id("txtUName").send_keys("88890032513")
        # 3.输入密码
        self.driver.find_element_by_id("txtPassword").send_keys("19980502")
        # 4.点击登录按钮
        self.driver.find_element_by_id("btnLogin").click()
        # 5.获取错误提示信息
        sleep(2)
        msg = self.driver.find_element_by_id("LabErr").text
        # 断言
        print("提示信息：", msg)

    def test_wrong_password(self):
        """密码错误"""

        # 1.点击首页的”登录“链接，进入登录页面
        # self.driver.find_element_by_partial_link_text("登录").click()
        # 2.输入用户名
        self.driver.find_element_by_id("txtUName").send_keys("13039131596")
        # 3.输入错误密码
        self.driver.find_element_by_id("txtPassword").send_keys("123450")
        # 4.点击登录按钮
        self.driver.find_element_by_id("btnLogin").click()
        # 5.获取错误提示信息
        sleep(2)
        msg = self.driver.find_element_by_id("LabErr").text
        # 断言
        print("提示信息：", msg)


if __name__ == '__main__':
    pytest.main(['-s', 'test_Login_3.py'])
