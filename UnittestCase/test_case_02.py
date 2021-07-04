import unittest
import requests
from unittest import mock
class SendRequest:
    def send_get(self, url, data, method):
        if method == 'get':
            res = requests.get(url, data).json()
            return res

    def send_post(self, url, data, method):
        if method == 'post':
            res = requests.post(url, data).json()
            return res
class TestLogin(unittest.TestCase):
    def setUp(self):
        print('case开始执行')

    def tearDown(self):
        print('case执行结束')

    def test_01(self):
        url = 'http://127.0.0.1:5000/login'
        data = {
            'username':'huangjaija',
        }
        sen = SendRequest()
        data1 = '缺少参数'
        sen.send_get = mock.Mock(return_value=data1)
        res = sen.send_get(url, data, 'get')

        self.assertEqual('缺少参数', res)
'''
if __name__ == '__main__':
    unittest.main()'''