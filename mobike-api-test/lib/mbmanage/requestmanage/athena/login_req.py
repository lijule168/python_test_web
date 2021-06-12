# /usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangjieran@mobike.com'

from lib.mbmanage.requestmanage.base_req import BaseReq

class LoginReq(BaseReq):

    def __init__(self):
        super(LoginReq,self).__init__()

    def user_login(self,param_dict=None, header_dict=None):
        '''
        登录web页面
        '''
        return  self.request("POST", "athena/weblogin/userlogin.do",params=param_dict, headers=header_dict)

