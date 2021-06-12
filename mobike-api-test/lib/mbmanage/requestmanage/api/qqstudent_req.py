#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangjieran'

from lib.mbmanage.requestmanage.base_req import BaseReq
class QQStudentReq(BaseReq):
    '''
    合作方发优惠券
    '''
    def __init__(self):
        super(QQStudentReq, self).__init__()

    def qqfans_getmobile(self, param_dict=None, header_dict=None):
        '''
        QQ学生认证用户确认。内部接口，由摩拜H5调用
        '''
        return self.request("GET", "api/v2/qqfans/getMobile", params=param_dict, headers=header_dict)

    def qqfans_confirm(self, param_dict=None, header_dict=None):
        '''
        QQ学生认证用户确认。外部接口，由QQ一方调用
        '''
        return self.request("POST", "api/v2/qqfans/confirm", params=param_dict, headers=header_dict)

