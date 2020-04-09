__author__ = '土豆'
import  cx_Oracle
import os

class OracleUtil:

    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

    def __init__(self):

        self.con = cx_Oracle.connect('shubcust1c/V2pa_4akN@134.64.11.34:1522/BSSA10G3')
        self.cursor = self.con.cursor()

    def fetch_one(self, sql):
        self.cursor.execute(sql)
        results=self.cursor.fetchone()
        if results:
            return results
        else:
            print("没有获取到值")


    def fetch_all(self, sql):
        self.cursor.execute(sql)
        results=self.cursor.fetchall()
        return results


    def deldata(self,sql):
        self.cursor.execute(sql)
        self.con.commit()



    def close(self):
        self.cursor.close()
        self.con.close()


if __name__ == '__main__':
    sql='select * from tf_f_company  order by company_id desc '
    sql2='select * from tf_f_customer order by customer_id desc'
    f=OracleUtil().fetch_all(sql)
    print(f)


    # import cx_Oracle
    #
    #
    #
    # connection = cx_Oracle.connect("Booker", "123456", "172.18.240.31:1521/Book")
    #
    # cursor = connection.cursor()
    # cursor.execute("select * from book")
    #
    # a = cursor.fetchall()
    #
    # cols = [d[0] for d in cursor.description]
    #
    # print(cols)
    #
    # for row in a:
    #     b = dict(zip(cols, row))
    #     print(b['book_name'])
    #
    # cursor.close()
    #
    # connection.close()