import json
import unittest
from parameterized import parameterized
import time

from mytest.myproject.login.loginpage import ProxyPage
from mytest.myproject.login.loginutil import LoginUtil, get_title, get_msg
from mytest.myproject.testcase.screenshot import screenshot


def test_data():
    """测试数据方法"""
    data_list = []
    with open("E:/web_auto_wh/mytest/myproject/login/test_data.json", encoding="utf-8") as f:
        datas = json.load(f)
        for data in datas.values():
            data_list.append((data["username"],
                              data["pwd"],
                              data["code"],
                              data["is_success"],
                              data["expect"]))
        return data_list
class TestLogin(unittest.TestCase):

    # 类模块,所有测试开始前运行
    @classmethod
    def setUpClass(cls):
        # 实例化一个浏览器对象
        cls.driver = LoginUtil.get_driver()
        cls.logintests = ProxyPage()

    # 类模块,所有测试结束后运行
    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        LoginUtil().quit_driver()

    # 方法模块,每条测试开始前运行
    def setUp(self):
        # 打开首页
        self.driver.get("http://localhost")
        # 如果无账号登录点击登录,已登录则点击安全退出再登录
        if self.driver.find_element_by_class_name("red").text == "登录":
            # 点击登录
            self.driver.find_element_by_class_name("red").click()
        else:
            self.driver.find_element_by_link_text("安全退出").click()
            self.driver.find_element_by_class_name("red").click()

    def tearDown(self):
        # 每条用例执行完等待两秒
        time.sleep(2)

    @parameterized.expand(test_data())
    def test_1(self, username, pwd, code, is_success, expect):
        """登录模块测试"""
        self.logintests.loginproxy(username, pwd, code)

        if is_success:
            msg = get_title()
            self.assertIn(expect, msg)
        else:
            time.sleep(1)
            screenshot()
            msg = get_msg()
            self.assertIn(expect, msg)