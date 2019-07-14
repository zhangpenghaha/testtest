# 元素层类
from selenium.webdriver.common.by import By

from mytest.myproject.login.BasePage import ElementBase, HandleBase
from mytest.myproject.login.loginutil import LoginUtil


class ElementPaga(ElementBase):
    """定位元素"""

    def __init__(self):
        # 实力化一个浏览器驱动对象
        super().__init__()

        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.verify_code = (By.ID, "verify_code")
        self.login_btn = (By.NAME, "sbtbutton")

    def find_username(self):
        return self.element_find(self.username)

    def find_pwd(self):
        return self.element_find(self.password)

    def find_code(self):
        return self.element_find(self.verify_code)

    def find_login_btn(self):
        return self.element_find(self.login_btn)

# 操作层
class HandlePage(HandleBase):

    def __init__(self):
        self.handle = ElementPaga()

    def input_username(self,username):
        self.input_text(self.handle.find_username(), username)

    def input_pwd(self,pwd):
        self.input_text(self.handle.find_pwd(), pwd)

    def input_code(self,code):
        self.input_text( self.handle.find_code(), code)

    def login_click(self):
        self.handle.find_login_btn().click()

class ProxyPage(object):

    def __init__(self):
        self.proxy = HandlePage()

    def loginproxy(self, username, pwd, code):
        self.proxy.input_username(username)
        self.proxy.input_pwd(pwd)
        self.proxy.input_code(code)
        self.proxy.login_click()


if __name__ == "__main__":

    ProxyPage().loginproxy("13333333333", "123456", "8888")
