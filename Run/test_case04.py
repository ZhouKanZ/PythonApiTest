import json
from time import time
import requests
import unittest
from Handle.handle_ini import handleini
from Handle.handle_excel import handleexcel
from Handle.handle_mysql import DB


'''首页数据接口'''

class TestCase04(unittest.TestCase):

    def setUp(self):
        print('开始执行用例')

    def tearDown(self):
        print('结束执行用例')

    def test_01(self):
        url = handleini.get_ini_value('test_server', 'host') + '/homepage/show-report'
        data = {
            'userID': '5e5czG - k8le - di7axABmUTFHEuKQ8q6h9mVbaOY3KgFjNw',
            'token': 'BVEMQ9sMdK2aSS15M7p906fs0WS1fyF0',
            'salt': '1',
            'timestamp': ',',
            'sign': ''
        }
        res = requests.post(url, data).json()
        DataBase = DB('timing')
        key_ = '59643'
        sql = "select fansCount from t_user where ID = '%s' "
        db_feed = DataBase.mysql_select(key_, sql)
        try:
            self.assertEqual(res['fansCount'], db_feed)
            print('昨日粉丝数量展示正确')
        except Exception as e:
            print('昨日粉丝数量不正确')

    def test_02(self):
        url = handleini.get_ini_value('test_server', 'host') + '/homepage/show-report'
        data = {
            'userID': '5e5czG - k8le - di7axABmUTFHEuKQ8q6h9mVbaOY3KgFjNw',
            'token': 'BVEMQ9sMdK2aSS15M7p906fs0WS1fyF0',
            'salt': '1',
            'timestamp': ',',
            'sign': ''
        }
        res = requests.post(url, data).json()
        DataBase = DB('timing_cp')
        key_ = '59643'
        sql = "select count(userID) from t_user_follow where followUserID = '%s' and DATE(postTime) = date_sub(curdate(),interval 1 day)%"
        db_feed = DataBase.mysql_select(key_, sql)
        try:
            self.assertEqual(res['increaseFansCount'], db_feed)
            print('昨日新增粉丝数量展示正确')
        except Exception as e:
            print('昨日新增粉丝数量不正确')

    def test_03(self):
        url = handleini.get_ini_value('test_server', 'host') + '/homepage/show-report'
        data = {
            'userID': '5e5czG - k8le - di7axABmUTFHEuKQ8q6h9mVbaOY3KgFjNw',
            'token': 'BVEMQ9sMdK2aSS15M7p906fs0WS1fyF0',
            'salt': '1',
            'timestamp': ',',
            'sign': ''
        }
        res = requests.post(url, data).json()
        DataBase = DB('timing_cp')
        key_ = '59643'
        sql = "select count(userID) from t_ where user_follow = '%s' and post_time between '2020-06-30 23:59:59' and '2020-07-01 00:00:00'"
        db_feed = DataBase.mysql_select(key_, sql)
        try:
            self.assertEqual(res['increaseFansCount'], db_feed)
            print('本月新增粉丝数量展示正确')
        except Exception as e:
            print('本月新增粉丝数量不正确')

if __name__ == '__main__':
    unittest.main()