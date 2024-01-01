from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///D:/pycharm_project/Newstu_Project/bli_stu/test_alert.html'
        self.driver.get(file_path)

    def test_alert(self):
        self.driver.find_element(By.ID, 'alert').click()
        # 切换到alert
        alert = self.driver.switch_to.alert
        print(alert.text)
        sleep(2)
        alert.accept()

    def test_confirm(self):
        self.driver.find_element(By.ID, 'confirm').click()
        confirm = self.driver.switch_to.alert
        print(confirm.text)
        sleep(3)
        confirm.dismiss()

    def test_prompt(self):
        self.driver.find_element(By.ID, 'prompt').click()
        sleep(2)
        prompt = self.driver.switch_to.alert
        print(prompt.text)
        sleep(2)
        prompt.accept()
        sleep(3)

        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.test_alert()
    # case.test_confirm()
    case.test_prompt()