# test_mouse  ---鼠标单击、双击、右击操作
# test_key    ---键盘输入内容、键盘control+A/x/v操作;鼠标移动并点击操作

from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_mouse(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        # 双击
        btn = self.driver.find_element(By.XPATH, '/html/body/form/input[2]')
        ActionChains(self.driver).double_click(btn).perform()
        sleep(2)
        # 单击
        btn = self.driver.find_element(By.XPATH, '/html/body/form/input[3]')
        ActionChains(self.driver).click(btn).perform()
        sleep(2)
        # 右击
        btn = self.driver.find_element(By.XPATH, '/html/body/form/input[4]')
        ActionChains(self.driver).context_click(btn).perform()
        sleep(5)

        self.driver.quit()

    def test_key(self):
        self.driver.get('http://www.baidu.com')
        kw = self.driver.find_element(By.ID, 'kw')
        kw.send_keys('好运连连！')
        kw.send_keys(Keys.CONTROL, 'a')
        sleep(2)
        kw.send_keys(Keys.CONTROL, 'x')
        sleep(2)
        kw.send_keys(Keys.CONTROL, 'v')
        sleep(2)

        # 鼠标移动到新闻，然后点击
        self.driver.get('http://www.baidu.com')
        e = self.driver.find_element(By.LINK_TEXT, '新闻')
        print(e)
        sleep(1)
        ActionChains(self.driver).move_to_element(e).click(e).perform()
        sleep(2)

        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.test_mouse()
    case.test_key()
