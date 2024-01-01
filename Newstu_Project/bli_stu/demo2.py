from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///D:/pycharm_project/Newstu_Project/bli_stu/from2.html'
        self.driver.get(file_path)

    def test_select(self):
        se = self.driver.find_element(By.ID, 'provide')
        select = Select(se)
        # 单选
        # select.select_by_index(2)
        # sleep(2)
        # select.select_by_value('cs')
        # sleep(2)
        # select.select_by_visible_text('Beijing')
        # sleep(2)

        # 多选
        # for i in range(3):
        #     select.select_by_index(i)
        #     sleep(1)
        # sleep(3)

        # 反选
        # select.deselect_all()
        # sleep(3)

        # 显示所有选项！！！！！！
        for option in select.options:
            print(option.text)

        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_select()
