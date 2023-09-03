"""测试用例
测试对象：act环境 https://act.hnkzy.com
"""

import unittest
import time
from parameterized import parameterized  # 引入parameterized模块
from selenium import webdriver


class TestLogin(unittest.TestCase):
    """
    1.打开浏览器：就使用setUp(self)方法打开浏览器
    2.查找用户名输入框
    3.查找密码的输入框
    4.点击登录
    5.断言登录成功与否 使登录后的页面上的用户名进行断言
    """

    # 创建登录数据，这里可以写多个账号进行测试  组织测试数据 格式[( ), ( ), ( )],一个元组就是一组测试数据
    # data=[
    #     ('账号','密码'),
    #     ('账号', '密码'),
    #     ('账号', '密码'),
    # ]

    data = [
        ('17608419842', '17608419842Aym'),
        ('18890032513', 'Aym19980623'),
        ('16636361111', 'Aym19980623'),
    ]

    def setUp(self) -> None:
        # 创建一个浏览器对象
        self.driver = webdriver.Chrome("D:/python3.9.10/chromedriver.exe")
        # 发送请求
        self.driver.get("https://act.hnkzy.com")

    def tearDown(self) -> None:
        # 关闭浏览器
        self.driver.close()
        # 退出浏览器
        self.driver.quit()

    @parameterized.expand(data)  # 参数化，在测试方法上方使用装饰器 @parameterized.expand(测试数据)
    def test_login(self, username, password):
        # 查找输入账号的文本框，并输入账号

        time.sleep(2)
        self.driver.find_element_by_id("loginUn").clear()  # 清空原文本框内容
        self.driver.find_element_by_id("loginUn").send_keys(username)  # 输入账号
        # 查找输入密码的文本框，并输入密码
        time.sleep(2)
        self.driver.find_element_by_id("loginPwd").clear()  # 清空原密码框内容
        self.driver.find_element_by_id("loginPwd").send_keys(password)  # 输入密码

        time.sleep(5)

        self.driver.find_element_by_xpath('//*[@id="loginForm"]/button/span[1]').click()

        time.sleep(2)
        # 断言登录是否成功
        # handle=self.driver.current_window_handle
        # self.driver.swtich_to.window(handle)
        # index=self.driver.find_element_by_xpath('//*[@id="admui-siteConTabs"]/div[1]/ul/li/a/span').text
        # 进行断言，如果在登录后的界面出现“首页”二字，就代表成功，否则视为失败   ？？？不晓得为什么初始的测试步骤通过不了
        # self.assertEqual(index,"首页",msg="登录失败")

        # 获取登录后页面的URL地址 index存入
        index = self.driver.current_url
        print(index)
        # 现改为判断登录后的URL是否与预期一致，若一致则登录成功。
        self.assertEqual(index, "https://act.hnkzy.com/console/main/index.html?_=1", msg="登录失败")
