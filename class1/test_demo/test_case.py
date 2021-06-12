import pytest

from api_demo.demo import data

'''
pytest 默认不输出任何打印信息,如果要看打印信息,要加 -s 

'''
#测试用例
def test_02():

    print('test02')
@data('')
def test_01():
    print('test_01')



def  setup_function():
    print('我是 function 开始')

def  teardown_function():
    print('我是 function  结束')

# def setup_module():
#     print('我是 module 开始')
#
# def teardown_module():
#     print('我是 module teardown 结束')


#pytest 中class  的定义:建议test 开头
class Cema:

    def setup(self):
        print('setup')

    @pytest.mark.webui
    def test_d1(self):
        print('test_d1')

    def test_d2(self):
        print('test_d2')

    def teardown(self):
        print('teardown')
    def setup_method(self):
        print('setup-module-start')

    def teardown_method(self):
        print('teardown-module-end ')

    def setup_class(self):
        print('setup-class-start')
    def teardown_class(self):
        print('teardown-class-end')

if __name__ == '__main__':
    pytest.main(['-s','-v','-rA','test_case.py'])
