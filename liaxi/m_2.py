# 在一个测试类中定义多个测试方法，查看每个测试方法执行完所花费的时

import unittest

import time


def myadd(a, b):
    return (a + b)


# 定义测试类  ---  必须继承unittest.TestCase
class TestFixture(unittest.TestCase):
    # 重写父类的setUpClass方法--类级别Fixture -- 测试类中所有测试方法-执行前自动执行
    @classmethod
    def setUpClass(cls):
        print("测试开始 %s" % time.time())


    # 重写父类的tearDownClass方法--类级别Fixture -- 测试类中所有测试方法-执行后自动执行
    @classmethod
    def tearDownClass(cls):
        print("测试结束 %s" % time.time())


    # 定义测试方法 --- 方法名必须是test开头
    def test_01(self):
        print("test_01")

    def test_02(self):
        print("test_02")
