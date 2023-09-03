# 一个页面封装成一个对象：应用：继承base
from v4 import page
from v4.base.base import Base


class PageLogin(Base):
    # 点击登录连接
    def page_click_login_link(self):
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_password(self, pwd):
        self.base_input(page.login_password, pwd)

    # # 输入验证码
    # def page_input_verify_code(self, code):
    #     self.base_input(page.login_verify_code, code)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取异常提示信息
    def page_get_error_info(self):
        return self.base_get_text(page.login_err_text)

    # 截图
    def page_get_screenshot(self):
        self.base_get_image()

    # 组合业务方法
    def page_login(self, username, password):
        page.login_username(username)
        page.login_password(password)
        # page.login_verify_code(code)
        page.login_btn()
