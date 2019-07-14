

# 页面元素层
from selenium.webdriver.common.by import By

from mytest.myproject.register.base_reg import BasePage, BaseHandle


class UtilPage(BasePage):
    def __init__(self):
        super().__init__()
        self.username = (By.NAME, "username")
        self.code = (By.NAME, "verify_code")
        self.pwd = (By.NAME, "password")
        self.pwd2 = (By.NAME, "password2")
        self.invite = (By.NAME, "invite")
        self.regbtn = (By.CLASS_NAME, "regbtn")

    def find_username(self):
        return self.emt_fd(self.username)
    def find_code(self):
        return self.emt_fd(self.code)
    def find_pwd(self):
        return self.emt_fd(self.pwd)
    def find_pwd2(self):
        return self.emt_fd(self.pwd2)
    def find_invite(self):
        return self.emt_fd(self.invite)
    def find_regbtn(self):
        return self.emt_fd(self.regbtn)

# 操作层
class PageHandle(BaseHandle):
    def __init__(self):
        self.reg_hand = UtilPage()

    def input_username(self, username):
        self.input_text(self.reg_hand.find_username(),username)

    def input_code(self, code):
        self.input_text(self.reg_hand.find_code(), code)

    def input_pwd(self, pwd):
        self.input_text(self.reg_hand.find_pwd(),pwd)

    def input_pwd2(self, pwd2):
        self.input_text(self.reg_hand.find_pwd2(), pwd2)

    def input_invite(self, invite):
        self.input_text(self.reg_hand.find_invite(),invite)

    def click_regbtn(self):
        self.reg_hand.find_regbtn().click()

# 业务层
class ProxyPage(object):
    def __init__(self):
        self.reg_pro = PageHandle()

    def reg_proxy(self, username, code, pwd, pwd2, invite):
        self.reg_pro.input_username(username)
        self.reg_pro.input_code(code)
        self.reg_pro.input_pwd(pwd)
        self.reg_pro.input_pwd2(pwd2)
        self.reg_pro.input_invite(invite)
        self.reg_pro.click_regbtn()
