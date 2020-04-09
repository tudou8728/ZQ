import unittest

from   common import contants, logger,context
from common.do_oracle import OracleUtil
from common.context import ReadConfig
from   common.do_excel import DoExcel
from   common.request import Request
from   libext.ddtnew import ddt, data

logger = logger.get_logger(logger_name='资质资料查询')

@ddt
class QualificationInqueryTest(unittest.TestCase):
    request = Request()
    config = ReadConfig()
    GetData = OracleUtil()
    do_excel = DoExcel(contants.case_file)
    cases = do_excel.get_cases('资质资料查询')
    def setUp(self):
        pass

    @data(*cases)
    def test_JC(self,case):
        logger.info("开始执行第{0}用例".format(case.id))
        certNum = self.config.get('data', 'certNum_1')
        if case.id == 1:
            certType = self.config.get('data', 'certType_1')
            setattr(context.Context, 'certType', certType)
            setattr(context.Context, 'certNum', certNum)
        else:
            sql_1 = "select * from tf_f_company  where cert_num='{}'".format(certNum)
            tf_f_company = self.GetData.fetch_one(sql_1)
            company_id = tf_f_company[0]
            sql_2 = "select * from tf_f_company_cust where company_id='{0}'".format(company_id)
            tf_f_company_cust = self.GetData.fetch_one(sql_2)
            customerId = tf_f_company_cust[1]
            sql_3 = "select * from tf_f_company_data_bing where company_id='{0}'".format(company_id)
            tf_f_company_data_bing = self.GetData.fetch_one(sql_3)
            tradeId = tf_f_company_data_bing[10]
            table = tradeId[0:6]
            sql_6 = "select * from tf_B_Trade_{0} where trade_id='{1}'".format(table, tradeId)
            tf_b_trade = self.GetData.fetch_one(sql_6)
            bmsAcceptId = tf_b_trade[25]
            setattr(context.Context, 'customerId', str(customerId))
            setattr(context.Context, 'bmsAcceptId', str(bmsAcceptId))
            setattr(context.Context, 'companyId', str(company_id))
            setattr(context.Context, 'tradeId', str(tradeId))
        case.data =context.replace(case.data)
        print("请求参数是：", case.data)
        resp = self.request.request(case.method, case.url, case.data)
        print(resp.json())
        try:
            self.assertEqual(case.expected, resp.json()['respDesc'], "api error ")
            self.do_excel.write_result('资质资料查询',case.id + 1, resp.text, 'PASS')
            logger.info("第{0}用例执行结果：PASS".format(case.id))
        except AssertionError as e:
            self.do_excel.write_result('资质资料查询',case.id + 1, resp.text, 'FAIL')
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