"""创建一个浏览器初始化和关闭的模块"""

from selenium import webdriver

# 创建一个初始化驱动对象类
class DriverPay():
    # 定义一个类属性
    _driver = None
    @classmethod
    def get_driver(cls):
        #如果没有浏览器驱动对象,则创建一个
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)
            cls._driver.get("http://localhost")
        return cls._driver

    @classmethod
    def quit_driver(cls):
        # 如果浏览器驱动对象部位空,则关闭浏览器并初始化为空
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None