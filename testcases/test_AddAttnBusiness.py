import unittest
from   common import contants, logger,context
from common.do_oracle import OracleUtil
from   common.do_excel import DoExcel
from   common.request import Request
from   libext.ddtnew import ddt, data
from common.context import ReadConfig

logger = logger.get_logger(logger_name='授信业务新增')

@ddt
class AddAttnBusiness(unittest.TestCase):
    request = Request()
    config = ReadConfig()
    GetData = OracleUtil()
    do_excel = DoExcel(contants.case_file)
    cases = do_excel.get_cases('授信业务新增')
    print(cases)

    def setUp(self):
        pass
    @data(*cases)
    def test_credit(self,case):
        logger.info("开始执行第{0}用例".format(case.id))
        print("转换前的参数是：",case.data)
        if case.id==1:
            certNum= self.config.get('data', 'certNum_1')
            certType=self.config.get('data', 'certType_1')
            setattr(context.Context, 'certType', certType)
            setattr(context.Context, 'certNum', certNum)
        elif case.id==2:
            certNum = self.config.get('data', 'certNum_1')
            sql_1 = "select * from tf_f_company  where cert_num='{}'".format(certNum)
            tf_f_company = self.GetData.fetch_one(sql_1)
            company_id = tf_f_company[0]
            sql_5 = "select * from tf_f_company_attn  where company_id='{0}'".format(company_id)
            tf_f_company_attn = self.GetData.fetch_one(sql_5)
            certType = tf_f_company_attn[2]
            certNum = tf_f_company_attn[3]
            setattr(context.Context, 'companyId', str(company_id))
            setattr(context.Context, 'certType', '0' + str(certType))
            setattr(context.Context, 'certNum', str(certNum))
        case.data = context.replace(case.data)
        print("转换后的参数是：", case.data)
        resp = self.request.request(case.method, case.url, case.data)
        print(resp.json())
        try:
            self.assertEqual(case.expected, resp.json()['respDesc'], "api error ")
            self.do_excel.write_result('授信业务新增',case.id + 1, resp.text, 'PASS')
            logger.info("第{0}用例执行结果：PASS".format(case.id))
        except AssertionError as e:
            self.do_excel.write_result('授信业务新增',case.id + 1, resp.text, 'FAIL')
            logger.error("第{0}用例执行结果：FAIL".format(case.id))
            raise e

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.request.close()
        certNum_1 = cls.config.get('data', 'certNum_1')
        sql_1 = "select * from tf_f_company  where cert_num='{}'".format(certNum_1)
        tf_f_company = cls.GetData.fetch_one(sql_1)
        company_id = tf_f_company[0]
        sql_2 = "delete from tf_F_COmpany_cust where company_ID = '{}'".format(company_id)
        sql_3 = "delete from tf_F_COMPANY where company_ID = '{}'".format(company_id)
        sql_4 = "delete from TF_F_COMPANY_CERT where company_ID = '{}'".format(company_id)
        sql_5 = "delete from TF_F_COMPANY_ATTN where  company_ID = '{}'".format(company_id)
        sql_6 = "delete from TF_F_COMPANY_INTRODUCTION where company_ID = '{}'".format(company_id)
        sql_7 = "delete from TF_F_COMPANY_INTRODUCTION where company_ID = '{}'".format(company_id)
        sql_8 = "delete from TF_F_COMPANY_QUALIFICATION where company_ID = '{}'".format(company_id)
        sql_9 = "delete from TF_F_COMPANY_DATA_BING where company_ID ='{}'".format(company_id)
        cls.GetData.deldata(sql_2)
        cls.GetData.deldata(sql_3)
        cls.GetData.deldata(sql_4)
        cls.GetData.deldata(sql_5)
        cls.GetData.deldata(sql_6)
        cls.GetData.deldata(sql_7)
        cls.GetData.deldata(sql_8)
        cls.GetData.deldata(sql_9)
        cls.GetData.close()