from mytest.dingdan.driver_util import DriverPay


class UtilPage:
    def __init__(self):
        self.driver = DriverPay().get_driver()



if __name__ == "__main__":
    UtilPage()