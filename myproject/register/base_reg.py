from mytest.myproject.register.util_reg import DriverReg


class BasePage():
    def __init__(self):
        self.driver = DriverReg().get_driver()
    def emt_fd(self,location):
        return self.driver.find_element(*location)

class BaseHandle():
    def input_text(self,inputtext, username):
        inputtext.send_keys(username)