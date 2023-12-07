import time
import unittest
from time import sleep
from selenium import webdriver

class TestLoginyx(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://202.111.177.155:8081/manager/static/ng-ant-admin/index.html#/login/login-form")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        sleep(5)
        self.driver.quit()

    def test_loginyx(self):
        driver=self.driver
        driver.find_element_by_css_selector(".ng-tns-c58-2 > .ant-input").click()
        driver.find_element_by_css_selector(".ant-input-status-success").send_keys("admin")
        driver.find_element_by_css_selector(".ng-untouched").send_keys("123456")
        driver.find_element_by_css_selector(".ant-btn").click()
        sleep(3)
        login_link=self.driver.current_url
        assert login_link=="http://202.111.177.155:8081/manager/static/ng-ant-admin/index.html#/default/dashboard/workbench"














