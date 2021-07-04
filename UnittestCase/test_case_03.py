import unittest
from unittest.mock import patch
class PayApi:
    @staticmethod
    def auth(card, amount):
        pass
    def pay(self, user_id, card, amount):
        response = self.auth(card, amount)
        try:
            if response['status_code'] == '200':
                print('用户{}支付金额{}成功'.format(user_id, amount))
                return '支付成功'
            elif response['status_code'] == '500':
                print('用户{}支付失败, 金额不变'.format(user_id))
                return '支付失败'
            else:
                return '未知错误'
        except Exception:
            return "Error, 服务器异常!"

class TestPay(unittest.TestCase):
    @patch.object(PayApi, 'auth')
    def test_01(self, mock_auth):
        mock_auth.return_value = {'status_code': '200'}
        Pay = PayApi()
        status = Pay.pay('1000', '2000', '3000')
        self.assertEqual(status, '支付成功')



if __name__ == '__main__':
    unittest.main()
