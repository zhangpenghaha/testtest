"""需求:
1. 点击登录按钮,进入登录页面
2. 输入用户名和密码, 不输入验证码,直接点击登陆
3 获取错误提示信息"""

# 导包
import unittest
import time
from selenium import webdriver

# 定义测试类
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://localhost")

    def tearDown(self):
        self.driver.quit()


    # 定义测试方法
    def test_login(self):
        # 业务操作
        time.sleep(3)
        # 1. 点击登录按钮,进入登录页面
        self.driver.find_element_by_link_text("登录").click()

        # 2. 输入用户名和密码, 不输入验证码,直接点击登陆
        self.driver.find_element_by_id("username").send_keys("13333333333")
        self.driver.find_element_by_id('password').send_keys("123456")
        self.driver.find_element_by_name("sbtbutton").click()

        # 3 获取错误提示信息
        text1 = self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
        print(text1)

        # 4 断言错误提示信息是否为"验证码不能为空",如果断言失败则保存截图
        try:
            self.assertIn("验证码不能为空1", text1)
        except AssertionError as A:
            # 保存图片
            self.driver.get_screenshot_as_file("./img/ %s.png" % time.strftime("%Y%m%d-%H%M%S"))
            print(type(A))
            raise A