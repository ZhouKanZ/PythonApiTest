import json
import time
import ddt
import unittest
from Handle.handle_ini import handleini
from Handle.handle_excel import handleexcel
from Base.BseRequest import baserequest
from Handle.handle_sign import creat_sign
from Handle.handle_result import get_result_json, handle_result_json
data = handleexcel.get_excel_data(2)
'''作品管理模块'''
@ddt.ddt
class TestCase02(unittest.TestCase):
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
            if assert_method == 'result':
                try:
                    self.assertTrue(res['result'])
                    handleexcel.write_excel_data(i, 11, '执行成功', 2)
                    handleexcel.write_excel_data(i, 12, json.dumps(res, ensure_ascii=False), 2)
                except Exception as e:
                    handleexcel.write_excel_data(i, 11, '执行失败', 2)
                    handleexcel.write_excel_data(i, 12, json.dumps(res, ensure_ascii=False), 2)
            if assert_method == 'json':
                url = data[3]
                json_data = get_result_json(url, 'success')
                try:
                    self.assertTrue(handle_result_json(res, json_data))
                    handleexcel.write_excel_data(i, 11, '执行成功', 2)
                    handleexcel.write_excel_data(i, 12, json.dumps(res, ensure_ascii=False), 2)
                except Exception as e:
                    handleexcel.write_excel_data(i, 11, '执行失败', 2)
                    handleexcel.write_excel_data(i, 12, json.dumps(res, ensure_ascii=False), 2)


if __name__ == '__main__':
    unittest.main()
'''
def jsonFormat(inputStr,count):
    if not isinstance(inputStr, dict):
        raise Exception("您传入的参数不是Dict，请检查入参")
    result = '{'

    for key, value in inputStr.items():
        result += '\n'
        if isinstance(value, dict):
            count += 1
            result += '\t' * count + key + ":" + jsonFormat(value, count) + ","
            count -= 1
        else:
            result += '\t'*(count+1)+key+":"+value+","
    result = result[:-1]
    result += '\n'+'\t'*count+'}'
    return result


if __name__ == '__main__':
    jsonStr = {
        "name": 'jiajia',
        "age": '18',
        'content':{
            'contry':'cn',
            'motherLag':'chinese',
            'info':{
                "url":"xxx.com"
            }
        }
    }
    print(jsonFormat(jsonStr,0))
'''