# 创建浏览器驱动基类
import time
from selenium import webdriver


class LoginUtil(object):
    # 创建类属性
    _driver = None

    # 创建获取浏览器驱动类方法
    @classmethod
    def get_driver(cls):
        """如果为空,创建一个浏览器驱动对象
           如果不为空, 返回这个浏览器属性"""
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(20)
            cls._driver.get("http://localhost")
        return cls._driver

    # 创建关闭浏览器类方法
    @classmethod
    def quit_driver(cls):
        """如果浏览器对象不为空,则可以关闭浏览器
           并将其赋值为空
           如果为空则不动作"""
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None

def get_msg():
    return LoginUtil().get_driver().find_element_by_class_name("layui-layer-content").text

def get_title():
    time.sleep(5)
    return LoginUtil().get_driver().title