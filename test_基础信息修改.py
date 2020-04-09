# -*- coding:utf-8 _*-
import unittest
import json
from faker import Faker
from   common import contants, logger,context
from common.config import  ReadConfig
from common.do_oracle import OracleUtil
from common.sql import GetCustData,GetCopmayData,GetDataBingData
from   common.do_excel import DoExcel
from   common.request import Request
from   libext.ddtnew import ddt, data

logger = logger.get_logger(logger_name='case')

@ddt
class pdateGrpCertInfoTest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)
    cases = do_excel.get_cases('集团基础信息修改')
    request = Request()
    config = ReadConfig()
    certNum_1 = config.get('data', 'certNum_1')
    GetData = OracleUtil()

    def setUp(self):

        sql_1 = "select * from tf_f_company  where cert_num='{}'".format(self.certNum_1)
        tf_f_company = self.GetData.fetch_one(sql_1)
        companyPost = tf_f_company[5]
        f = GetCopmayData()
        c = GetCustData()
        b = GetDataBingData()
        customerId = c.get_customerId()
        certType = f.get_certType()
        certNum = f.get_certNum()
        certExpireDate = f.get_certExpireDate()
        companyName = f.get_companyName()
        companyPhone = f.get_companyPhone()
        companyAddress = f.get_companyAddress()
        contactMan = f.get_contactMan()
        tradeId = b.get_tradeid()
        marketingUtil = f.get_marketingUtil()
        custManagerName = f.get_custManagerName()
        remark = f.get_remark()

        setattr(context.Context, 'customerId', str(customerId))
        setattr(context.Context, 'certType', str(certType))
        setattr(context.Context, 'certNum', str(certNum))
        setattr(context.Context, 'certExpireDate', str(certExpireDate))
        setattr(context.Context, 'companyName', str(companyName))
        setattr(context.Context, 'companyPost', str(companyPost))
        setattr(context.Context, 'companyPhone', str(companyPhone))
        setattr(context.Context, 'companyAddress', str(companyAddress))
        setattr(context.Context, 'contactMan', str(contactMan))
        setattr(context.Context, 'tradeId', str(tradeId))
        setattr(context.Context, 'marketingUtil', str(marketingUtil))
        setattr(context.Context, 'custManagerName', str(custManagerName))
        setattr(context.Context, 'remark', str(remark))
    @data(*cases)
    def test_updateGrpCertInfo(self,case):
        logger.info("开始执行第{0}条用例".format(case.id))
        case.data = context.replace(case.data)
        print("请求前参数是：", case.data)
        case.data=json.loads(case.data)
        ran=Faker(locale='zh_CN')
        if case.id==3:
            case.data['companyInfo']['companyPost']=ran.postcode()
        if case.id==4:
            case.data['companyInfo']['marketingUtil'] = ran.user_name()
        if case.id==5:
            case.data['companyInfo']['custManagerName'] = ran.name()
        if case.id==6:
            case.data['companyInfo']['remark'] = ran.sentence()
        if case.id==7:
            case.data['companyInfo']['contactMan'] = ran.name()
        if case.id==8:
            case.data['companyInfo']['companyAddress'] = ran.address()
        if case.id==9:
            case.data['companyInfo']['companyPhone'] = ran.phone_number()
        if case.id==10:
            case.data['companyInfo']['companyPhone'] = ran.email()
        case.data=json.dumps(case.data)
        print("请求后参数是：", case.data)
        resp = self.request.request(case.method, case.url, case.data)
        print(resp.json())
        try:
            self.assertEqual(case.expected, resp.json()['respDesc'], "api error ")
            f = GetCopmayData()
            if case.id==3:
                # config = ReadConfig()
                # certNum_1 = config.get('data', 'certNum_1')
                # GetData = OracleUtil()
                sql_1 = "select * from tf_f_company  where cert_num='{}'".format(self.certNum_1)
                tf_f_company = self.GetData.fetch_one(sql_1)
                companyPost=tf_f_company[5]
                case.data = json.loads(case.data)
                self.assertEqual(int(case.data['companyInfo']['companyPost']),int(companyPost),"data error")
            self.do_excel.write_result('集团基础信息修改',case.id + 1, resp.text, 'PASS')
            logger.info("第{0}用例执行结果：PASS".format(case.id))
        except AssertionError as e:
            self.do_excel.write_result('集团基础信息修改',case.id + 1, resp.text, 'FAIL')
            logger.error("第{0}用例执行结果：FAIL".format(case.id))
            raise e

    def tearDown(self):
        pass