'''
这是 pytest 中 setUp 和 tearDown 的配置文件

scope 参数定义了四种登记
session : 每一次的运行
module: 在模块中执行一次
class: 在类级别中只执行一次
function: 在每个函数中执行一次
默认登记是 function
'''


import pytest

#定义一个基本的 setUp 和 tearDown

@pytest.fixture(scope='session')
def xuzhu():
    print('xuzhu 生病了,但是很强')


@pytest.fixture(scope='module')
def xuzhu1():
    print('xuzhu 生病了,但是很强000002222')
    return 2