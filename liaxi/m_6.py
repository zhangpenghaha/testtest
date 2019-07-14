#导包
import unittest

from day4.a_1 import TestAdd

# HTMLTestRunner

# 定义测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestAdd))
# 测试报告存放路径
report_path = "E:\web_auto_wh\mytest"

# 打开文件
with open(report_path, "wb") as f:
    f
    # 实例化运行器对象
    # HTMLTestRunner(f, tital="TPshop项目自动化测试报告", )