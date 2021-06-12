'''
pytest 中用例的管理手段
可以通过Mark 装饰器对所有用例进行标记,不同的标记区分进行管理

 --self-contained-html 将测试报告生成一个文件
如果要集成到邮件,需要添加这个指令

-s -v -rA 添加了这个后,就不会生成错误的信息
'''
import pytest

@pytest.mark.webui
def viptest_01(xuzhu1):
    assert xuzhu1 == 1, '失败'
    # print('web01')

@pytest.mark.webui
def test_02():
    print('web02')
@pytest.mark.interface
def test_03():
    print('web03')
@pytest.mark.interface
@pytest.mark.temp
def test_04():
    print('web04')


if __name__ == '__main__':
    pytest.main(['-s','test_case3.py'])
