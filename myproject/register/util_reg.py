from selenium import webdriver


class DriverReg(object):
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)
            cls._driver.get("http://localhost")
        return cls._driver
    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None

def get_msg():
    return DriverReg().get_driver().find_element_by_class_name("layui-layer-content").text
