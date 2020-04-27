
import unittest
import json
from   common import contants, logger,context
from   common.do_excel import DoExcel
from   common.request import Request
from   libext.ddtnew import ddt, data
from common.context import ReadConfig
logger = logger.get_logger(logger_name='证件照片上传')


@ddt
class UploadImgTest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)  # 传入cases.xlsx
    cases = do_excel.get_cases('证件照片上传')
    request = Request()
    def setUp(self):
        pass

    @data(*cases)
    def test_uploadImg(self,case):
        logger.info("开始执行第{0}用例".format(case.id))
        if case.id == 1:
            case.data = json.loads(case.data)
            case.data['imgId'] = ReadConfig().get('data', 'imgId')
            case.data = json.dumps(case.data)
            case.data = context.replace(case.data)
        case.data=context.replace(case.data)
        print("请求参数是：", case.data)
        resp = self.request.request(case.method, case.url, case.data)
        print(resp.json())
        try:
            self.assertEqual(case.expected, resp.json()['respDesc'], "api error ")
            self.do_excel.write_result('证件照片上传',case.id + 1, resp.text, 'PASS')
            logger.info("第{0}用例执行结果：PASS".format(case.id))
            if resp.json()['respDesc']=="查询成功":
                imgContent=resp.json()['imgContent']
                setattr(context.Context, 'imgContent', str(imgContent))
        except AssertionError as e:
            self.do_excel.write_result('证件照片上传',case.id + 1, resp.text, 'FAIL')
            logger.error("第{0}用例执行结果：FAIL".format(case.id))
            raise e

    def tearDown(self):
        pass