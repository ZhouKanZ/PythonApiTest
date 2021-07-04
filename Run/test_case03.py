import json
from time import time
import requests
import ddt
import unittest
from Handle.handle_ini import handleini
from Handle.handle_excel import handleexcel
from Base.BseRequest import baserequest
from Handle.handle_mysql import DB
from Handle.handle_sign import creat_sign
from HTMLTestRunner import HTMLTestRunner
'''视频数据模块'''

class TestCase03(unittest.TestCase):
    def setUp(self):
        print('开始执行用例')
    def tearDown(self):
        print('结束执行用例')
    def test_01(self):
        url = handleini.get_ini_value('test_server', 'host') + '/homepage/feed-list'
        data = {
            "userID":"82e0HmjMGTGQcAdVPkKd8Xx1w0-eXMCjno2_FNHahqTMgQ",
            "token": "58HJBBYd_RB9FVOHiIlrYts8M5vpKzrk",
            "page": "1",
            "orderType": "2",
            "orderField": "postTime",
            "salt": "1",
            "timestamp": str(round(time() * 1000)),
            "sign": ""
        }
        data['sign'] = creat_sign(data)
        res = requests.post(url, data).json()
        DataBase = DB('timing_cp')
        key_ = '59643'
        sql = "select * from tc_feed where user_id = '%s' order by create_time desc limit 10"
        db_feed = DataBase.mysql_select(key_, sql)
        keys = []
        for i in range(10):
            type_data = res['list'][i]['id']
            keys.append(type_data)
        self.assertEqual(keys, db_feed)

    def test_02(self):
        url = handleini.get_ini_value('test_server', 'host') + '/homepage/feed-list'
        data = {
            "userID": "82e0HmjMGTGQcAdVPkKd8Xx1w0-eXMCjno2_FNHahqTMgQ",
            "token": "58HJBBYd_RB9FVOHiIlrYts8M5vpKzrk",
            "page": "1",
            "orderType": "2",
            "orderField": "postTime",
            "salt": "1",
            "timestamp": str(round(time() * 1000)),
            "sign": ""
        }
        data['sign'] = creat_sign(data)
        res = requests.post(url, data).json()
        DataBase = DB('timing')
        key_ = '29277'
        sql = "select likeCount from t_learning_feed where id = '%s' order by postTime desc"
        db_feed = DataBase.mysql_select(key_, sql)
        real_count = res['list'][0]['likeCount']
        print(real_count, db_feed)
        try:
            self.assertEqual(real_count, db_feed)
            print('点赞数量正确')
        except Exception as e:
            print('点赞数量不正确')
    def test_03(self):
        url = handleini.get_ini_value('test_server', 'host') + '/homepage/feed-list'
        data = {
            "userID":"82e0HmjMGTGQcAdVPkKd8Xx1w0-eXMCjno2_FNHahqTMgQ",
            "token": "58HJBBYd_RB9FVOHiIlrYts8M5vpKzrk",
            "page": "1",
            "orderType": "2",
            "orderField": "postTime",
            "salt": "1",
            "timestamp": str(round(time() * 1000)),
            "sign": ""
        }
        data['sign'] = creat_sign(data)
        res = requests.post(url, data).json()
        DataBase = DB('timing')
        key_ = '29277'
        sql = "select replyCount from t_learning_feed where id = '%s' order by postTime desc"
        db_feed = DataBase.mysql_select(key_, sql)

        real_count = res['list'][0]['replyCount']
        try:
            self.assertEqual(real_count,db_feed)
            print('评论数量正确')
        except Exception as e:
            print('评论数量不正确')
    '''
    def test_04(self):
        url = handleini.get_ini_value('test_server', 'host') + '/homepage/feed-list'
        data = {
            "userID":"82e0HmjMGTGQcAdVPkKd8Xx1w0-eXMCjno2_FNHahqTMgQ",
            "token": "58HJBBYd_RB9FVOHiIlrYts8M5vpKzrk",
            "page": "1",
            "orderType": "2",
            "orderField": "postTime",
            "salt": "1",
            "timestamp": str(round(time() * 1000)),
            "sign": ""
        }
        data['sign'] = creat_sign(data)
        res = requests.post(url, data).json()
        DataBase = DB('timing')
        key_ = '29277'
        sql = "select shareCount from t_learning_feed where id = '%s' order by postTime desc"
        db_feed = DataBase.mysql_select(key_, sql)
        real_count = res['list'][0]['shareCount']
        try:
            self.assertEqual(real_count, db_feed)
            print('转发数量正确')
        except Exception as e:
            print('转发数量不正确')
'''

suite = unittest.TestSuite()
suite.addTest(TestCase03('test_01'))
suite.addTest(TestCase03('test_02'))
suite.addTest(TestCase03('test_03'))
with open('D:\\dev\\python_project\\PythonApiTest\\Case\\report.html', 'w', encoding='utf-8') as f1:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f1, title='测试报告练习', description='试试水')
    runner.run(suite)
    f1.close()