# 业务层 导包调用page页面
import unittest
from v4.page.page_login import PageLogin
from parameterized import parameterized


def get_data():
    return [("130391315961", "123456", "手机号格式不正确！"),
            ("18890032513", "123456", "验证码不正确!")]


# 新建测试类 并 继承
class TestLogin(unittest.TestCase):
    login = None

    # setUp

    @classmethod
    def setUpClass(cls):
        # 实例化 获取页面对象 PageLogin
        cls.login = PageLogin()
        # 点击登录连接
        cls.login.page_click_login_link()

    # tearDown
    @classmethod
    def tearDownClass(cls):
        # 关闭 driver驱动对象
        cls.login.driver.quit()

    # 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, pwd, expect_result):
        # 调用登录方法
        self.login.page_login(username, pwd)
        # 获取登录提示信息
        msg = self.login.page_get_error_info()
        try:
            # 断言
            self.assertEqual(msg, expect_result)
        except AssertionError:
            # 截图
            self.login.page_get_img()
