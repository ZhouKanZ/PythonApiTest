import json
import time
import ddt
import unittest
from Handle.handle_ini import handleini
from Handle.handle_excel import handleexcel
from Base.BseRequest import baserequest
from Handle.handle_sign import creat_sign
data = handleexcel.get_excel_data(1)
@ddt.ddt
class TestCase05(unittest.TestCase):
    @ddt.data(*data)
    def test_01(self, data):
        is_run = data[2]
        case_id = data[0]
        i = handleexcel.get_row_number(case_id, 0)
        if is_run == 'yes':
            request_url = handleini.get_ini_value('test_server', 'host') + data[3]
            request_method = data[6]
            request_data = json.loads(data[7])
            t = time.time()
            request_data['timestamp'] = str(round(t * 1000))
            request_data['sign'] = creat_sign(request_data)
            res = baserequest.run_main(request_method, request_url, request_data)
            assert_method = data[9]
            expected_result = data[10]
            real_result = res['errorMsg']
            if assert_method == 'result':
                try:
                    self.assertTrue(res['result'])
                    handleexcel.write_excel_data(i, 12, '执行成功', 1)
                    handleexcel.write_excel_data(i, 13, json.dumps(res, ensure_ascii=False), 1)
                except Exception as e:
                    handleexcel.write_excel_data(i, 12, '执行失败', 1)
                    handleexcel.write_excel_data(i, 13, json.dumps(res, ensure_ascii=False), 1)
            if assert_method == 'eM':
                try:
                    self.assertEqual(expected_result, real_result)
                    print(expected_result, res['errorMsg'])
                    handleexcel.write_excel_data(i, 12, '执行成功', 1)
                    handleexcel.write_excel_data(i, 13, json.dumps(res, ensure_ascii=False), 1)
                except Exception as e:
                    handleexcel.write_excel_data(i, 12, '执行失败', 1)
                    handleexcel.write_excel_data(i, 13, json.dumps(res, ensure_ascii=False), 1)

if __name__ == '__main__':
    unittest.main()