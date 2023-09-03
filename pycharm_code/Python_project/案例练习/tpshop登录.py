"""
    目标：断言练习
    案例：
        输入：正确用户名和密码 验证码为空
        断言：提示信息是否为 验证码不能为空
        要求：如果断言出错 截屏保存
"""
#导包
import time
import unittest
from time import sleep
from selenium import webdriver
# 导包
import unittest

from selenium import webdriver


#定义测试类并继承unittest.TestCase
class TestTphopLogin(unittest.TestCase):
    def setUp(self):
        #获取浏览器驱动对象
        self.driver=webdriver.Chrome()
        #打开URL
        self.driver.get("http://gztsg.teetron.com.cn")
        #最大化浏览器
        self.driver.maximize_window()
        #隐士等待
        self.driver.implicitly_wait(20)

    #定义teardown
    def tearDown(self):
        #关闭浏览器驱动
        sleep(3)
        self.driver.quit()


    #定义登录测试方法 验证码为空
    def test_login_code_null(self):
        driver = self.driver
        #点击登录连接
        driver.find_element_by_partial_link_text("登录").click()
        #输入用户名
        driver.find_element_by_css_selector("#userName").send_keys("18890032513")
        #输入密码
        driver.find_element_by_css_selector("#userPwd").send_keys("123456")
        #输入验证码
        driver.find_element_by_css_selector("[name=validateCode]").send_keys("  ")
        #点击登录
        driver.find_element_by_css_selector("#login").click()
        #获取登录后提示信息
        result=driver.find_element_by_css_selector("#error").text
        print("rusult:",result)
        #定义预期结果
        expect_result="验证码不正确!."
        try:
            #断言
            self.assertEqual(result,expect_result)
        except AssertionError:
            #截图
            driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))
            #抛异常
            raise