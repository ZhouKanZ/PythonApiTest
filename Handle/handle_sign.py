import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
import hashlib
def get_sign(data):
    keys = []
    dict_data = ''
    data.pop('sign')
    for key in data:
        keys.append(key)
    keys.sort()
    for i in range(len(keys)):
        dict_data = dict_data + keys[i] + '=' + data[keys[i]] + '&'
    dict_data = dict_data + 'privateKey' + '=' + 'TZOTZqpsREJ601tN0Sa9nkD40TFZ6it8'
    return dict_data

def creat_sign(data):
    res = get_sign(data)
    md5 = hashlib.md5()
    md5.update(res.encode('utf-8'))
    return md5.hexdigest()
