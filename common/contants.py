# -*- coding:utf-8 _*-
""" 

"""
import os


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
data_dir = os.path.join(base_dir, "datas")

case_file = os.path.join(data_dir, "cases.xlsx")

conf_dir = os.path.join(base_dir, "conf")

test_conf = os.path.join(conf_dir, "test.conf")
test2_conf = os.path.join(conf_dir, "test2.conf")
global_conf = os.path.join(conf_dir, "global.conf")

logs_dir = os.path.join(base_dir, "logs")

testcases_dir = os.path.join(base_dir, "testcases")

reports_dir = os.path.join(base_dir, 'reports')
reports_html = os.path.join(reports_dir, 'reports.html')