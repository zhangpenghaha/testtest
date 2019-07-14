import unittest

import time
from selenium import webdriver

class TestLogin(unittest.TestCase):

    def test_login(self):
        """用户登录模块测试"""
        driver = webdriver.Chrome()
        driver.get("http://localhost")
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.find_element_by_link_text("登录").click()
        driver.find_element_by_id("username").send_keys("1333333333")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id('verify_code').send_keys("8888")
        title1 = driver.title
        driver.find_element_by_link_text("登    录").click()
        time.sleep(3)
        titil2 = driver.title
        self.assertNotEqual(title1,titil2)
if __name__ == "__main__":
    unittest.main()
# suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(TestLogin))
# runner = unittest.TextTestRunner()
# runner.run(suite)