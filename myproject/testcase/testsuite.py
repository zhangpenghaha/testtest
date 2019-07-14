import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from mytest.myproject.login.logintest import TestLogin
from mytest.myproject.register.test_reg import TestRegister

class TestTpshop(unittest.TestSuite):
    def test_suite(self):
        self.suite = unittest.TestSuite()
        self.suite.addTest(unittest.makeSuite(TestLogin))
        self.suite.addTest(unittest.makeSuite(TestRegister))

        with open("./report/TPshop.html", "wb") as f:
            runner = HTMLTestRunner(f, title="TPshop商城自动化测试报告", description="Chrome" )
            runner.run(self.suite)

if __name__ =="__main__":
    TestTpshop().test_suite()

