import pymysql

class DB():
    '''
    连接数据库、创建游标
    '''
    def __init__(self, database, host='rds7r40uo8u5s5xy0y9p0public.mysql.rds.aliyuncs.com', user='timing_backend', password='timing_backend_gyag2s'):
        self.myconnect = pymysql.connect(host, user, password, database)
        self.mycursor = self.myconnect.cursor()

    '''  
    在游标上面写查询语句
    '''
    def return_cursor(self):
        return self.mycursor


    def mysql_select(self, data, select_sql):
        select_cursor = self.return_cursor()

        sql = select_sql%(data)
        select_cursor.execute(sql)
        results = select_cursor.fetchone()
        return results
'''
DataBase = DB('timing_cp')
if __name__ == '__main__':
    print(DataBase.mysql_select(60178, "select * from tc_feed where user_id = '%s' order by create_time desc"))
    '''



