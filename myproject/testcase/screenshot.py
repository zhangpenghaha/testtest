import time

from mytest.myproject.login.loginutil import LoginUtil


def screenshot():
    driver = LoginUtil().get_driver()
    driver.get_screenshot_as_file("E:/web_auto_wh/mytest/myproject/testcase/report/{}.png".format(time.strftime("%Y%m%d%H%M%S")))