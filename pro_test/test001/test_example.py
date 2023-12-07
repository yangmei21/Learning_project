# coding=utf-8
from selenium import webdriver
import unittest
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class TestLogin(unittest.TestCase):
    # 指定浏览器
    def setUp(self):
        self.driver = webdriver.Firefox()
        # 打开url
        self.driver.get("http://192.168.10.6/login")

    # 登录操作
    def test_login(self):
        title = self.driver.title
        print(title)
        now_url = self.driver.current_url
        print(now_url)
        username = "test001"
        password = "testgood001"
        # 执行登录操作
        # 用户名的定位
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        # 密码的定位
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)
        # 点击登录
        self.driver.find_element_by_css_selector(".btn.btn-success.btn-block").click()
        # 登录成功断言
        login_name = self.driver.find_element_by_xpath('html/body/div[3]/div[2]/ul/li[1]/a/strong').text
        login_name = login_name.strip('您好：')
        assert login_name == username

    # 关闭浏览器
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()