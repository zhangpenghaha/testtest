import time
import unittest

from selenium import webdriver

class TestZhuce(unittest.TestCase):
    def test_zhuce(self):
        """用户注册模块测试"""
        # 创建一个浏览器驱动对象
        driver = webdriver.Chrome()
        # 打开TPSHOP商城首页
        driver.get("http://localhost")
        # 窗口最大化
        driver.maximize_window()
        # 设置隐式等待30秒
        driver.implicitly_wait(30)

        # 点击注册按钮
        driver.find_element_by_link_text("注册").click()
        title1 = driver.title

        # 输入用户名
        driver.find_element_by_id("username").send_keys("13112346768")
        # 输入验证码
        driver.find_element_by_name("verify_code").send_keys("8888")
        # 输入密码
        driver.find_element_by_id("password").send_keys("123456")
        # 确认密码
        driver.find_element_by_id("password2").send_keys("123456")
        time.sleep(2)
        # 点击同意注册协议(默认已点击)
        # driver.find_element_by_class_name("iyes").click()

        # 点击同意注册
        driver.find_element_by_link_text("同意协议并注册").click()
        time.sleep(6)
        title12 = driver.title
        self.assertNotEqual(title1, title12)
        # 关闭浏览器驱动对象
        driver.quit()

if __name__ == "__main__":
    unittest.main()