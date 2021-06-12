#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangjieran@mobike.com'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName
from lib.util.log_util import l

class UserApiReq(BaseReq):
    # 接口wiki地址https://wiki.mobike.com/pages/viewpage.action?pageId=24123984
    def __init__(self):
        super(UserApiReq, self).__init__(micro_service_name=MicroServiceName.USER_API)

    def get_contract_status_req(self, param_dict, header_dict):
        '''
        查询用户是否同意过条款
        '''
        l.info("查询用户是否同意过条款")
        return self.request("POST", "usercontract/getcontractstatus", params=param_dict, headers=header_dict)

    def change_contract_status_req(self, param_dict, header_dict):
        '''
        修改用户条款同意状态
        '''
        l.info("修改用户条款同意状态")
        return self.request("POST", "usercontract/changecontractstatus", params=param_dict, headers=header_dict)

    def getUserRegionByMobile(self, param_dict=None):
        '''
        根据mobile获取region
        :param mobile
        :return:
        '''
        l.info("根据mobile获取region")
        return self.request("GET", "userregion/getUserRegionByMobile.do", params=param_dict)
    def get_prainfo_req(self, header_dict):
        '''
        查询用户隐私
        '''
        l.info("查询用户隐私")
        return self.request("POST", "globaluserextendinfo/getprainfo.do", headers=header_dict)

    def update_prainfo_req(self, param_dict, header_dict):
        '''
        更新用户隐私
        '''
        l.info("更新用户隐私")
        return self.request("POST", "globaluserextendinfo/updateprainfo.do", params=param_dict, headers=header_dict)


    def clear_prainfo_req(self,header_dict):
        '''
        清空用户隐私
        '''
        l.info("清空用户隐私")
        return self.request("POST", "globaluserextendinfo/clearprainfo.do", headers=header_dict)