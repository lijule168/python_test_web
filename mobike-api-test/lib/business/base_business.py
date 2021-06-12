# /usr/bin/python
# -*- coding:utf-8 -*-
from script.assert_util import AssertUtil
import json

class BaseBusiness(object):
    def __init__(self):
        pass

    def init_params(self, local_vars_copy):
        '''
        请求参数,自动赋值
        :param local_vars_copy:
        :return: 处理后的请求参数
        '''
        if 'self' in local_vars_copy:
            local_vars_copy.pop('self')

        param_dict = local_vars_copy.copy()
        header_dict = {}
        file_dict = {}
        for key in local_vars_copy:
            if local_vars_copy[key] is None:
                param_dict.pop(key)
                continue
            if key.__contains__("__py_debug_temp"):
                param_dict.pop(key)
            if key.startswith('header_'):
                param_dict.pop(key)
                header_key = key.split('_')[1]
                header_dict[header_key] = local_vars_copy[key]
            elif key.startswith('file_'):
                param_dict.pop(key)
                file_key = key.split('_')[1]
                file_dict[file_key] = local_vars_copy[key]
            elif key.startswith('param_'):
                param_dict.pop(key)
                param_key = key.split('_')[1]
                param_dict[param_key] = local_vars_copy[key]

        return (header_dict, param_dict, file_dict,)

    def init_response(self, local_vars_copy, instance, func_name, if_assert=1,
                      assert_str='{"code":0, "message":"成功"}', msg=''):
        '''
        请求参数自动赋值，返回接口返回值，支持断言
        :param local_vars_copy:请求接口的参数
        :param instance:接口所在的实例
        :param func_name:接口名称
        :param if_assert:是否做断言
        :param assert_str:断言需要的值（字典）
        :param msg:若断言失败，需要输出的提示
        :return:返回接口的返回值
        '''
        header_dict, param_dict, file_dict = self.init_params(local_vars_copy)
        try:
            param_dict.pop("if_assert")
            param_dict.pop("assert_str")
            param_dict.pop("msg")
        except:
            pass
        response = getattr(instance, func_name)(param_dict=param_dict, header_dict=header_dict)
        if if_assert:
            if isinstance(assert_str, str):
                assert_str = json.loads(assert_str)
            AssertUtil.assert_key_value_in_list(assert_str, response, msg=msg+str(response))
        return response




