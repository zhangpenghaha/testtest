import unittest
import time
class TestFixture(unittest.TestCase):

    # 初始化,前置处理,首先自动的执行
    def setUp(self):
        print("start time:", time.time())

    # 销毁,后置处理,最后自动的执行
    def tearDown(self):
        print("end time:", time.time())

    def test01(self):
        print("test01")

    def test02(self):
        print("test02")
