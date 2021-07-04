import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
import json

def load_json():
    file_path = r'D:\dev\python_project\PythonApiTest\Config\result.json'
    with open(file_path, encoding='utf-8') as f:
        data =json.load(f)
    return data
def get_value(key):
    data = load_json()
    return data[key]

if __name__ == '__main__':
    print(get_value('/feed/list'))