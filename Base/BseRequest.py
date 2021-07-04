import requests
import json

class BaseRequest():
    def send_post(self,url,data):
        '''
        封装post请求方式
        '''
        res = requests.post(url=url, data=data).text
        return res

    def send_get(self,url,data):
        '''
        封装get请求方式
        '''
        res = requests.get(url=url, parames=data).text
        return res


    def run_main(self,method,url,data):
        '''
        通过method值判断发送哪一种类型的请求
        '''
        if method == 'post':
            res = self.send_post(url, data)
        else:
            res = self.send_get(url, data)
        try:
            res = json.loads(res)
        except:
            print("这个结果是一个text")
        return res

baserequest = BaseRequest()