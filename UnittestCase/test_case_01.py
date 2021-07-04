import threading
import time
import requests
import json

class BaseRequest(threading.Thread):

    def __init__(self, data):
        super().__init__()
        self.method = 'post'
        self.url = 'http://api.kr-cell.net/login-register/login-by-phone'
        self.data = data

    def send_post(self):
        '''
        封装post请求方式
        '''
        res = requests.post(self.url, self.data).text
        print(self.data)
        return res

    def send_get(self):
        '''
        封装get请求方式
        '''
        res = requests.get(self.url, self.data).text
        return res


    def run(self):#线程类需要运行的函数为名称为run,调用线程方法运行的就是threading 的run方法，定义线程类就要修改run方法从而生成线方法
        '''
        通过method值判断发送哪一种类型的请求
        '''
        if self.method == 'post':
            res = self.send_post()
        else:
            res = self.send_get()
        try:
            res = json.loads(res)
            print(res)
        except:
            print("这个结果是一个text")
        return res

def main():
    threads = []
    start = time.time()
    globals_data = threading.Thread()

    for i in range(10):
        global_data = {'phone': 10000000160+i, 'password': '111111', 'countryCode': '86'}
        t = BaseRequest(global_data)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    end = time.time()
    print('总共花费了%f秒'% (end-start))

if __name__ == '__main__':
    main()

