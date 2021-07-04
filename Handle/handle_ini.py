import os
import configparser

class HandleIni:

    def load_ini(self):
        file_path = 'D:\dev\python_project\PythonApiTest\Config\server.ini' #注意文件名称不要写错
        print(file_path)
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding='utf-8')
        return cf

    def get_ini_value(self, section, key):
        cf = self.load_ini()
        data = cf.get(section, key)
        return data


handleini = HandleIni()