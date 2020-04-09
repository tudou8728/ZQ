# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 20:43
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : math_sutie.py

import unittest
import HTMLTestRunnerNew
from common import contants
from testcases.test_GroupMaterialCreate import ATest
from testcases.test_bssGetAttnInfo import BssAttnInquiryTest

suite=unittest.TestSuite()

#loader加载方式
loader=unittest.TestLoader()
def add1():
    suite.addTest(loader.loadTestsFromTestCase(ATest))
def add2():
    suite.addTest(loader.loadTestsFromTestCase(BssAttnInquiryTest))
def insertData():
    for i in range(1, 100000):
        if i == 1:
           print("11111111")
           add1()
        if i == 99999:
            print("99999999")
            add2()
insertData()
with open(contants.reports_html, 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title='API',
                                              description='API测试报告',
                                              tester='S')
    runner.run(suite)