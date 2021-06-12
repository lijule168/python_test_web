#!/usr/bin/python
#-*- coding:utf-8 -*-

from lib.mbmanage.requestmanage.base_req import BaseReq

__author__ = 'dingbaixia@mobike.com'


class CurrentConfigReq(BaseReq):
    #新增对应类型的配置
    ADD_CONFIGBYTYPE = "athena/opsconfig/addConfigByType.do"
    #删除对应类型的配置
    DELETE_CONDFIG = "athena/opsconfig/deleteConfig.do"
    #查询对应类型的配置
    QUERY_CONFIGLIST = "athena/opsconfig/queryConfigList.do"

    def __init__(self):
        super(CurrentConfigReq, self).__init__()

    def addConfigByType(self, json_data=None):
        '''
        新增对应类型的配置
        :param json_data:
        :return:
        '''
        header_dict = {"Content-Type":"application/json;charset=UTF-8"}
        return self.request("POST", self.__class__.ADD_CONFIGBYTYPE, headers=header_dict, json_data=json_data)

    def deleteConfig(self, json_data=None):
        '''
        删除对应类型的配置
        :param json_data:
        :return:
        '''
        header_dict = {"Content-Type":"application/json;charset=UTF-8"}
        return self.request("POST", self.__class__.DELETE_CONDFIG, headers=header_dict, json_data=json_data)

    def queryConfigList(self, json_data=None):
        '''
        查询对应类型的配置
        :param json_data:
        :return:
        '''
        header_dict = {"Content-Type":"application/json;charset=UTF-8"}
        return self.request("POST", self.__class__.QUERY_CONFIGLIST, headers=header_dict, json_data=json_data)