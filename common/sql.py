# from common.do_oracle import OracleUtil
# from common.config import ReadConfig
#
#
#
# class GetCopmayData():
#     def __init__(self,sql_1):
#         GetData = OracleUtil()
#         self.tf_f_company = GetData.fetch_one(sql_1)
#
#     def get_companyId(self):
#         return self.tf_f_company[0]
#
#     def get_certType(self):
#         return self.tf_f_company[1]
#
#     def get_certNum(self):
#         return self.tf_f_company[2]
#
#     def get_companyName(self):
#         return self.tf_f_company[4]
#
#     def get_certExpireDate(self):
#         return str(self.tf_f_company[3]).strip('00:00:00')
#
#     def get_companyPost(self):
#         return self.tf_f_company[5]
#
#     def get_companyPhone(self):
#         return self.tf_f_company[6]
#
#     def get_companyAddress(self):
#         return self.tf_f_company[7]
#
#     def get_contactMan(self):
#         return self.tf_f_company[8]
#
#     def get_remark(self):
#         return self.tf_f_company[29]
#
#     def get_marketingUtil(self):
#         return self.tf_f_company[42]
#
#     def get_custManagerName(self):
#         return self.tf_f_company[43]
#
#
# class GetCustData:
#     def __init__(self,sql_1,sql_2):
#         company_id = GetCopmayData(sql_1).get_companyId()
#         GetData = OracleUtil()
#         # sql_2 = "select * from tf_f_company_cust where company_id='{0}'".format(company_id)
#         self.tf_f_company_cust = GetData.fetch_one(sql_2)
#
#     def get_customerId(self):
#         return  self.tf_f_company_cust[1]
#
#
#
#
# class GetDataBingData:
#     def __init__(self, sql_1, sql_3):
#         company_id = GetCopmayData(sql_1).get_companyId()
#         GetData = OracleUtil()
#         # sql_3 = "select * from tf_f_company_data_bing where company_id='{0}'".format(company_id)
#         self.tf_f_company_data_bing=GetData.fetch_one(sql_3)
#
#     def get_tradeid(self):
#         return self.tf_f_company_data_bing[10]
#
#
# class GetCertData:
#     def __init__(self, sql_1, sql_4):
#         company_id = GetCopmayData(sql_1).get_companyId()
#         GetData = OracleUtil()
#         # sql_4 = "select * from tf_f_company_cert  where company_id='{0}'".format(company_id)
#         self.tf_f_company_cert=GetData.fetch_one(sql_4)
#
#     def get_capital(self):
#         return self.tf_f_company_cert[10]
#
#     def get_certAddress(self):
#         return self.tf_f_company_cert[6]
#
#     def get_certExpireDate(self):
#         return self.tf_f_company_cert[7]
#
#     def get_certInfoId(self):
#         return self.tf_f_company_cert[0]
#
#     def get_certNum(self):
#         return self.tf_f_company_cert[4]
#
#     def get_certType(self):
#         return self.tf_f_company_cert[3]
#
#     def get_certName(self):
#         return self.tf_f_company_cert[5]

#
#     def get_imgId(self):
#         return self.tf_f_company_cert[12]
#
#     def get_imgType(self):
#         return self.tf_f_company_cert[12]
#
#     def get_infoType(self):
#         return self.tf_f_company_cert[2]
#
#     def get_legalRep(self):
#         return self.tf_f_company_cert[8]
#
#     def get_businessScope(self):
#         return self.tf_f_company_cert[9]
#
#     def get_issue(self):
#         return self.tf_f_company_cert[11]
#
#     def get_status(self):
#         return self.tf_f_company_cert[14]
#
#
#
#
# class GetAttnData:
#     def __init__(self, sql_1, sql_5):
#         company_id = GetCopmayData(sql_1).get_companyId()
#         GetData = OracleUtil()
#         # sql_5 = "select * from tf_f_company_attn  where company_id='{0}'".format(company_id)
#         self.tf_f_company_attn=GetData.fetch_one(sql_5)
#
#     def get_attncertnum(self):
#         return self.tf_f_company_attn[3]
#
#     def get_attncertype(self):
#         return self.tf_f_company_attn[2]
#
#
#
# class  GetTradeData:
#     def __init__(self, sql_1, sql_3,sql_6):
#         GetData = OracleUtil()
#         trade_id=GetDataBingData(sql_1,sql_3).get_tradeid()
#         table=trade_id[0:6]
#         # sql_6="select * from tf_B_Trade_{0} where trade_id='{1}'".format(table,trade_id)
#         self.tf_b_trade = GetData.fetch_one(sql_6)
#
#     def get_bmsAcceptId(self):
#         return self.tf_b_trade[25]
#
#
# if __name__ == '__main__':
#   print(GetTradeData().get_bmsAcceptId())
#   print(GetCopmayData().get_companyId())
#   print(GetCustData().get_customerId())