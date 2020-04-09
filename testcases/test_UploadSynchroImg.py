# -*- coding:utf-8 _*-
"""

@function：
"""
import unittest
from   common import contants, logger,context
from   common.do_excel import DoExcel
from   common.request import Request
from   libext.ddtnew import ddt, data

logger = logger.get_logger(logger_name='总部和政企照片同步上传')


@ddt
class UploadSynchroImgTest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)  # 传入cases.xlsx
    cases = do_excel.get_cases('总部和政企照片同步上传')
    request = Request()
    def setUp(self):
        pass

    @data(*cases)
    def test_uploadSynchroImg(self,case):
        logger.info("开始执行第{0}用例".format(case.id))
        case.data=context.replace(case.data)
        print("请求参数是：", case.data)
        resp = self.request.request(case.method, case.url, case.data)
        print(resp.json())
        try:
            self.assertEqual(case.expected, resp.json()['respDesc'], "api error ")
            self.do_excel.write_result('总部和政企照片同步上传',case.id + 1, resp.text, 'PASS')
            logger.info("第{0}用例执行结果：PASS".format(case.id))
        except AssertionError as e:
            self.do_excel.write_result('总部和政企照片同步上传',case.id + 1, resp.text, 'FAIL')
            logger.error("第{0}用例执行结果：FAIL".format(case.id))
            raise e

    def tearDown(self):
        pass