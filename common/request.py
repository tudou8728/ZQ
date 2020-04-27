# -*- coding:utf-8 _*-

import requests
import json
from common import logger
from common.config import ReadConfig
logger = logger.get_logger('request')


class Request:

    def __init__(self):
        self.session = requests.sessions.session()

    def request(self, method, url, data):
        method = method.upper()
        config = ReadConfig()
        pre_url=config.get('api','pre_url')
        url=pre_url+url
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        data = data.encode('UTF-8')
        logger.info('method: {0}  url: {1}'.format(method, url))
        logger.info('data: {0}'.format(data))

        if method == 'GET':
            resp = self.session.request(method, url, params=data)
            return resp

        elif method == 'POST':
            print(data)
            resp = self.session.request(method, url, data=data,headers=headers)
            logger.info('response: {0}'.format(resp.text))
            return resp
        else:
            logger.error('Un-support method !!!')
            pass

    def close(self):
        self.session.close()

if __name__ == '__main__':
    from common.do_excel import DoExcel
    do_excel = DoExcel('E:\\ZQ_code\datas\cases.xlsx')
    cases = do_excel.get_cases('继承')
    print(cases[3].method)
    print(cases[3].url)
    print(cases[3].data)
    request = Request().request(cases[3].method,cases[3].url,cases[3].data)
    print(request.text)
