from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///D:/pycharm_project/Newstu_Project/bli_stu/froms.html'
        self.driver.get(file_path)

    def test_login(self):
        self.driver.find_element(By.ID, 'username').send_keys('admin')
        self.driver.find_element(By.ID, 'pwd').send_keys('123456')
        sleep(1)
        self.driver.find_element(By.ID, 'submit').click()


if __name__ == '__main__':
    case = TestCase()
    case.test_login()
