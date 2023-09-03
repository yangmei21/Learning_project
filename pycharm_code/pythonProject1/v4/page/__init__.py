"""
以下为登录页面元素配置信息，临时存放地
"""
from selenium.webdriver.common.by import By

# 登录
login_link = By.PARTIAL_LINK_TEXT, "登录"
# 用户名
login_username = By.ID, "txtUName"
# 密码
login_password = By.ID, "txtPassword"
# 验证码
# login_verify_code=By.CSS_SELECTOR,"validateCode"
# 登录按钮
login_btn = By.ID, "btnLogin"
# 获取异常文本信息
login_err_text = By.ID, "LabErr"


# 登录页数据