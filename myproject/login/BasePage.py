from mytest.myproject.login.loginutil import LoginUtil


class ElementBase():

    def __init__(self):
        self.driver = LoginUtil().get_driver()

    # 定位元素基类
    def element_find(self, location):
        return self.driver.find_element(*location)



class HandleBase():
    # 输入类容基类
    def input_text(self, elet, text):
        elet.clear()
        elet.send_keys(text)