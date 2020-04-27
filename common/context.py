import re
import random
from faker import Faker
from common.config import ReadConfig
config = ReadConfig()


class Context:
    #继承的号码和类型
    certNum_1=config.get('data','certNum_1')
    certType_1 =config.get('data','certType_1')
    #获取组织机构代码校验
    certNum_2 = config.get('data', 'certNum_2')
    certType_2 = config.get('data', 'certType_2')
    ##订单是否绑定
    bmsAcceptId_1 =config.get('data', 'bmsAcceptId_1')
    bmsAcceptId_2 = config.get('data', 'bmsAcceptId_2')


def replace(data):
    p = "\$\{(.*?)}"
    while re.search(p, data):
        match = re.search(p, data)
        param = match.group(1)
        if hasattr(Context, param):
            v = getattr(Context, param)
            data = re.sub(p, v, data, count=1)
        else:
            return print("这个{}没有值".format(param))
    return data

#
# def get_name():
#     f = Faker(locale='zh_CN')
#     return f.name()
#
#
# def get_attnCertNum():
#     f = Faker(locale='zh_CN')
#     return f.ssn()
#
#
# def get_address():
#     f = Faker(locale='zh_CN')
#     return f.address()
#
#
# def get_phone():
#     f = Faker(locale='zh_CN')
#     return f.phone_number()
#
#
# def get_company():
#     f=Faker(locale='zh_CN')
#     return f.company()


if __name__ == '__main__':
    s='{"custName":"${name}","capital":"10000","certType":"06","certNum":"${certNum_1}","certAddress":"${address}","certExpireDate":"2037-01-01","infoType":"20000","imgId":"12345"}'
    f=replace(s)
    print(f)
