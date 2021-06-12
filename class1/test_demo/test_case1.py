import pytest



'''
pytest 默认不输出任何打印信息,如果要看打印信息,要加 -s 


#pytest 中的setup 和 teardown 有八个,
可以通过一个配置文件直接管理


'''


#测试用例
def test_02():
    print('test02')

def test_01():
    print('test_01')


if __name__ == '__main__':
    pytest.main(['-s','-v','-rA'])


