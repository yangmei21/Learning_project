"""
登录页面
课程居然不完整。。。啊啊啊
"""
from selenium.webdriver.common.by import By

from utils import DriverUtil


class LoginPage(object):
    """登录对象层"""

    def __init__(self):
        """获取浏览器对象"""
        self.driver = DriverUtil.get_driver()  # 获取浏览器对象
        # 将元素的定位方法及特征封装成属性，能够实现集中管理目标元素的定位方法及特征值
        self.name = (By.ID, 'txtUName')  # 用户名
        self.pwd = (By.ID, 'txtPassword')  # 密码
        self.btn = (By.ID, 'btnLogin')  # 登录

    def find_username(self):
        """定位用户名方法"""
        # return self.driver.find_element_by_id("txtUName")
        # return self.driver.find_element_by_id(By.ID,"txtUName")
        return self.driver.find_element(self.name[0], self.name[1])

    def find_password(self):
        """定位密码方法"""
        # return self.driver.find_element_by_id("txtPassword")
        return self.driver.find_element(self.pwd[0], self.pwd[1])

    def find_login_btn(self):
        # return self.driver.find_element_by_id("btnLogin")
        return self.driver.find_element(self.btn[0], self.btn[1])


class LoginHandle(object):
    """登录操作层"""

    def __init__(self):
        self.login_page = LoginPage()  # 获取对象层对象

    def input_username(self, name):
        """输入用户名方法"""
        # 说明：在执行输入操作前，应该先执行清空操作
        self.login_page.find_username().clear()
        self.login_page.find_username().send_keys(name)

    def input_password(self, password):
        """输入密码方法"""
        self.login_page.find_password().clear()
        self.login_page.find_password().send_keys(password)

    def click_login_btn(self):
        """点击登录按钮方法"""
        self.login_page.find_login_btn().click()


class LoginTask(object):
    """登录业务层"""

    def __init__(self):
        self.login_handle = LoginHandle()  # 获取操作层对象

    def login_method(self, name, password):
        """登录方法"""
        self.login_handle.input_username(name)  # 输入用户名
        self.login_handle.input_password(password)  # 输入密码
        self.login_handle.click_login_btn()  # 点击登录按钮
