#coding=utf-8
import configparser

class ConfigTools:

    def __init__(self,filepath):
        self.filepath = filepath
        self.inifile=configparser.ConfigParser()


    def get_err(self):
        print(self.filepath)

    # 获取配置文件中的元素
    def get_config(self,data):


        self.inifile.read(self.filepath, 'UTF-8')

        # print(self.inifile.get(data[0], data[1]))


        return self.inifile.get(data[0], data[1])

    # 修改或添加配置文件中的应用
    def update_config(self,data):
        # 添加新的配置文件,或修改配置
        self.inifile['web']['pwd'] = '198.333.444'

        with open(self.filepath, 'w') as config:
            self.inifile.write(config)
        return 'updata success'



#测试代码
# aa = '.\config.ini'
# tt=ConfigTools(aa)
#
# print(tt.get_config(['db','ip']))
# tt.get_err()
#
# print('aa')