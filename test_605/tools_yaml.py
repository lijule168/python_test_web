#encoding = utf-8
import  ddt


import unittest

# import yaml


@ddt.ddt
class TestCode(unittest.TestCase):



    @ddt.data(1,2,3)
    def test_data(self,value):
        print(value)

    @ddt.data([1,2],[3,4],[5,6])
    @ddt.unpack
    def test_ini(self,num1,num2):
        print(num1,num2)

    @ddt.file_data(".\ddt.yaml")
    def testcase(self, **kwargs):

        print(kwargs.get('username'))

        # for a in *args:
        #     print(a)



if __name__ == '__main__':
    unittest.main()