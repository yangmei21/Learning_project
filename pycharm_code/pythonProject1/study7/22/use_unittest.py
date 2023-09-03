# 查看是否正常登录
from time import sleep
import unittest
from selenium import webdriver

__author__ = 'Administrator'


class ZentaoTestByUnittest(unittest.TestCase):
    def setUp(self):
        # 设定一个base url，存储根目录的地址
        self.base_url = "http://novel.hctestedu.com/user/login.html"

        # 实例化火狐浏览器的对象
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # 退出火狐浏览器
        self.driver.quit()

    def test_login(self):
        driver = self.driver

        # 用get的方式，打开base url
        driver.get(self.base_url)

        # 让python休息2秒钟，给浏览器2秒时间加载页面
        sleep(2)

        # 查找登录页面的用户输入框，并把元素保存到account中
        account = driver.find_element_by_id("txtUName")

        # 清除 account 已经输入的字符，并输入 admin
        account.clear()
        account.send_keys("13039131596")

        # 查找登录页面的密码输入框，并把元素保存到 password 中
        password = driver.find_element_by_id("txtPassword")

        # 清除 password 已经输入的字符，并输入 123456
        password.clear()
        password.send_keys("123456")

        # 查找 保持登录 的元素（复选框），并打勾
        driver.find_element_by_id("autoLogin").click()

        # 查找 登录 的元素，点击登录
        driver.find_element_by_id("btnLogin").click()

        # 让python休息5秒钟，给火狐5秒时间加载页面
        sleep(5)

        # 做验证
        # 设定期望的结果
        # expected = self.base_url + "/index.php?m=my&f=989indes"
        expected = "http://novel.hctestedu.com/"
        # 获取实际的结果
        actual = driver.current_url

        self.assertEqual(expected, actual, "系统登录跳转主页失败！")


# 主方法的入口
if __name__ == "__main__":
    # 实例化一个ZentaoTest对象，调用它登录的方法
    unittest.main()
