import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from selenium import webdriver
from parameterized import parameterized
from mytest import users

# 生成用户注册信息并保存到card.txt中
def user_cards():
    return users.user(3)

def read_cards():
    with open("./card.txt", 'r') as f2:
        user_1 = f2.readlines()
        user_list = []
        for line in user_1:
            user_list.append(line.split(","))
    return user_list

class TestTP(unittest.TestCase):
    def setUp(self):
        # 创建一个浏览器驱动对象
        self.driver = webdriver.Chrome()
        # 打开TPshop商城主页
        self.driver.get("http://localhost")
        # 最大化浏览器
        self.driver.maximize_window()
        # 设置隐式等待30秒
        self.driver.implicitly_wait(30)

    def tearDown(self):
        # 关闭浏览器驱动对象
        self.driver.quit()

    @parameterized.expand(user_cards)
    def test_login(self,user,password,code):
        """注册模块测试"""
        # 点击注册按钮
        self.driver.find_element_by_link_text("注册").click()
        title1 = self.driver.title
        # 输入用户名
        self.driver.find_element_by_id("username").send_keys(user)
        # 输入验证码
        self.driver.find_element_by_name("verify_code").send_keys(code)
        # 输入密码
        self.driver.find_element_by_id("password").send_keys(password)
        # 确认密码
        self.driver.find_element_by_id("password2").send_keys(password)
        time.sleep(2)
        # 点击同意注册协议(默认已点击)
        # driver.find_element_by_class_name("iyes").click()
        # 点击同意注册
        self.driver.find_element_by_link_text("同意协议并注册").click()
        time.sleep(3)
        time.sleep(6)
        title12 = self.driver.title
        try:
            self.assertNotEqual(title1, title12)
        except AssertionError:
            self.driver.get_screenshot_as_file("./sreen/{}.png".format(time.strftime("%Y%m%d%H%M%S")))
            raise AssertionError

    @parameterized.expand(read_cards)
    def test_zhuce(self,user,password,code):
        """用户登录模块测试"""
        self.driver.find_element_by_link_text("登录").click()
        title1 = self.driver.title
        self.driver.find_element_by_id("username").send_keys(user)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id('verify_code').send_keys(code)
        self.driver.find_element_by_link_text("登    录").click()
        time.sleep(6)
        title2 = self.driver.title
        try:
            self.assertNotEqual(title1, title2)
        except AssertionError:
            self.driver.get_screenshot_as_file("./screen/{}.png".format(time.strftime("%Y%m%s%H%M%S")))
            raise AssertionError

# 创建一个测试套件实例
suite = unittest.TestSuite()
# 添加测试用例
suite.addTest(unittest.makeSuite(TestTP))
# 实例化一个运行器对象
with open("./baogao/{}.html".format(time.strftime("%Y%m%d%H%M%S")),'wb') as f:
    runner = HTMLTestRunner(f, title="TPshop测试报告")
    runner.run(suite)
