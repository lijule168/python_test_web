#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangsong'

from lib.mbmanage.requestmanage.base_req import BaseReq

class UserConnectionReq(BaseReq):

    #绑定亲密关系接口
    BIND_CONNECTION = "api/v2/userConnection/bindConnection.do"

    #解除亲密关系接口
    DISCONNECT = "api/v2/userConnection/disconnect.do"

    #查看亲密账户关系
    CHECK_CONNECTION = "api/v2/userConnection/checkConnection.do"

    # 未登录情况下查看邀请者信息
    GET_MASTER_INFO = "api/v2/userConnection/getMasterInfo.do"

    # 邀请者主动发起邀请
    BIND_SUB = "api/v2/userConnection/bindSub.do"

    def bind_sub_req(self, header={}, param={}):
        '''邀请者主动发起邀请'''
        return self.request("POST", UserConnectionReq.BIND_SUB, headers=header, params=param)

    def bind_connection_req(self, header={}, param={}):
        '''绑定亲密关系接口'''
        return self.request("POST", UserConnectionReq.BIND_CONNECTION, headers=header, params=param)

    def disconnect_req(self, header={}, param={}):
        '''解除亲密关系接口'''
        return self.request("POST", UserConnectionReq.DISCONNECT, headers=header, params=param)

    def check_connection_req(self, header={}, param={}):
        '''查看亲密账户关系'''
        return self.request("GET", UserConnectionReq.CHECK_CONNECTION, headers=header, params=param)

    def get_master_info_req(self, param={}):
        '''未登录情况下查看邀请者信息'''
        return self.request("GET", UserConnectionReq.GET_MASTER_INFO, params=param)