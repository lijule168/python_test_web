'''
pytest 中用例的管理手段
可以通过Mark 装饰器对所有用例进行标记,不同的标记区分进行管理
'''
import pytest

@pytest.mark.webui
def test_01():
    print('web01')

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
