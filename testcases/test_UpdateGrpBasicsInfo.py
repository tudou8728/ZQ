# -*- coding:utf-8 _*-
import json
import unittest

from faker import Faker

from common import contants, logger, context
from common.context import ReadConfig
from common.do_excel import DoExcel
from common.do_oracle import OracleUtil
from common.request import Request
from libext.ddtnew import ddt, data

logger = logger.get_logger(logger_name='集团基础信息修改')

@ddt
class UpdateGrpBasicsInfoTest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)
    cases = do_excel.get_cases('集团基础信息修改')
    request = Request()
    config = ReadConfig()
    GetData = OracleUtil()

    def setUp(self):
        pass

    @data(*cases)
    def test_updateGrpBasicsInfo(self,case):
        logger.info("开始执行第{0}条用例".format(case.id))
        print("请求前参数是：", case.data)
        certNum = self.config.get('data', 'certNum_1')
        if case.id == 1:
            certType = self.config.get('data', 'certType_1')
            setattr(context.Context, 'certType', certType)
            setattr(context.Context, 'certNum', certNum)
        else:
            sql_1 = "select * from tf_f_company  where cert_num='{}'".format(certNum)
            tf_f_company = self.GetData.fetch_one(sql_1)
            company_id = tf_f_company[0]
            certType = tf_f_company[1]
            certNum = tf_f_company[2]
            companyName = tf_f_company[4]
            sql_2 = "select * from tf_f_company_cust where company_id='{0}'".format(company_id)
            tf_f_company_cust = self.GetData.fetch_one(sql_2)
            customerId = tf_f_company_cust[1]
            sql_3 = "select * from tf_f_company_data_bing where company_id='{0}'".format(company_id)
            tf_f_company_data_bing = self.GetData.fetch_one(sql_3)
            tradeId = tf_f_company_data_bing[10]
            certExpireDate = str(tf_f_company[3]).strip('00:00:00')
            setattr(context.Context, 'customerId', str(customerId))
            setattr(context.Context, 'certType', str(certType))
            setattr(context.Context, 'certNum', str(certNum))
            setattr(context.Context, 'companyName', str(companyName))
            setattr(context.Context, 'tradeId', str(tradeId))
            setattr(context.Context, 'certExpireDate', str(certExpireDate))
            case.data=json.loads(case.data)
            ran=Faker(locale='zh_CN')
            case.data['companyInfo']['companyPost']=ran.postcode()
            case.data['companyInfo']['marketingUtil'] = ran.user_name()
            case.data['companyInfo']['custManagerName'] = ran.name()
            case.data['companyInfo']['remark'] = ran.sentence()
            case.data['companyInfo']['contactMan'] = ran.name()
            case.data['companyInfo']['companyAddress'] = ran.address()
            case.data['companyInfo']['companyPhone'] = ran.phone_number()
            case.data=json.dumps(case.data)
        case.data = context.replace(case.data)
        print("请求后参数是：", case.data)
        resp = self.request.request(case.method, case.url, case.data)
        print(resp.json())
        try:
            self.assertEqual(case.expected, resp.json()['respDesc'], "api error ")
            if case.id==2:
                config = ReadConfig()
                certNum_1 = config.get('data', 'certNum_1')
                GetData = OracleUtil()
                sql_1 = "select * from tf_f_company  where cert_num='{}'".format(certNum_1)
                tf_f_company = GetData.fetch_one(sql_1)
                marketingUtil=tf_f_company[42]
                custManagerName =tf_f_company[43]
                remark = tf_f_company[29]
                companyPost = tf_f_company[5]
                companyPhone = tf_f_company[6]
                companyAddress =tf_f_company[7]
                contactMan = tf_f_company[8]
                case.data = json.loads(case.data)
                self.assertEqual(case.data['companyInfo']['marketingUtil'], marketingUtil, "data error")
                self.assertEqual(case.data['companyInfo']['custManagerName'], custManagerName, "data error")
                self.assertEqual(case.data['companyInfo']['remark'], remark, "data error")
                self.assertEqual(int(case.data['companyInfo']['companyPost']),int(companyPost),"data error")
                self.assertEqual(int(case.data['companyInfo']['companyPhone']), int(companyPhone), "data error")
                self.assertEqual(case.data['companyInfo']['companyAddress'], companyAddress, "data error")
                self.assertEqual(case.data['companyInfo']['contactMan'], contactMan, "data error")
            self.do_excel.write_result('集团基础信息修改',case.id + 1, resp.text, 'PASS')
            logger.info("第{0}用例执行结果：PASS".format(case.id))
        except AssertionError as e:
            self.do_excel.write_result('集团基础信息修改',case.id + 1, resp.text, 'FAIL')
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