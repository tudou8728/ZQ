# -*- coding:utf-8 _*-
""" 

@function： 
"""
import unittest

from libext import HTMLTestRunnerNew

from common import contants


discover = unittest.defaultTestLoader.discover(contants.testcases_dir, pattern="test_*.py", top_level_dir=None)

with open(contants.reports_html, 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title='API',
                                              description='API测试报告',
                                              tester='S')
    runner.run(discover)
