import json
import unittest
from parameterized import parameterized
import time

from mytest.myproject.register.register_page import ProxyPage
from mytest.myproject.register.username import Reg_data
from mytest.myproject.register.util_reg import DriverReg, get_msg


def reg_data():
    Reg_data().is_success(3)
    reg_datas = []
    with open("E:/web_auto_wh/mytest/myproject/register/reg_data.json", encoding="utf-8") as f:
        datas = json.load(f)
        for data in datas.values():
            reg_datas.append((data["username"],
                              data["verify_code"],
                              data["pwd"],
                              data["pwd2"],
                              data["invite"],
                              data["expect"]))
    return reg_datas


class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 创建一个实例化浏览器驱动对象
        cls.driver = DriverReg().get_driver()
        cls.register_test = ProxyPage()
    @classmethod
    def tearDownClass(cls):
        DriverReg.quit_driver()

    def setUp(self):
        self.driver.get("http://localhost")
        # 如果注册成功,点击退出再进行下一条用例
        if self.driver.find_element_by_class_name("red").text == "登录":
            self.driver.find_element_by_link_text("注册").click()
        else:
            self.driver.find_element_by_link_text("安全退出").click()
            self.driver.find_element_by_link_text("注册").click()

    def tearDown(self):
        time.sleep(2)

    @parameterized.expand(reg_data)
    def testcase(self, username, verify_code, pwd, pwd2, invite, expect):
        """注册模块测试"""
        self.register_test.reg_proxy(username, verify_code, pwd, pwd2, invite)
        msg = get_msg()
        self.assertIn(expect, msg)