#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangjieran'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName
from lib.util.log_util import l

class OpRedisReq(BaseReq):

    OPREDIS_SET = "opredis/set"
    OPREDIS_GET = "opredis/get"
    OPREDIS_DELETE = "opredis/delete"
    OPREDIS_EXPIRE = "opredis/expire"

    OPREDIS_CONFIG_SET = "opredis/config/set"
    OPREDIS_CONFIG_QUERY = "opredis/config/query"

    def __init__(self):
        super(OpRedisReq, self).__init__(micro_service_name=MicroServiceName.SECURITY)

    def opredis_set_req(self, json_data):
        '''
        设置黑名单手机号
        :param json_dict: {"keyCode":0,"values":["123","456"]}
        :return:{"status": 1, "result": true, "errorMsg": ""}
        '''
        l.info("设置黑名单手机号")
        header_dict = {"Content-Type": "application/json"}
        return self.request("POST", self.OPREDIS_SET, json_data=json_data, headers=header_dict)

    def opredis_get_req(self, param_dict):
        '''
        获取黑名单手机号
        :param json_dict: keyCode=0&value=123
        :return:{"status": 1, "result": true, "errorMsg": ""}
        '''
        l.info("获取黑名单手机号")
        header_dict = {"Content-Type": "application/json"}
        return self.request("GET", self.OPREDIS_GET, params=param_dict)

    def opredis_delete_req(self, param_dict):
        '''
        删除黑名单手机号
        :param json_dict: keyCode=0&value=123
        :return:{"status": 1, "result": true, "errorMsg": ""}
        '''
        l.info("删除黑名单手机号")
        header_dict = {"Content-Type": "application/json"}
        return self.request("POST", self.OPREDIS_DELETE, params=param_dict)

    def opredis_expire_req(self, param_dict):
        '''
        设置黑名单有效期
        :param json_dict: keyCode=0&value=123
        :return:{"status": 1, "result": true, "errorMsg": ""}
        '''
        l.info("设置黑名单有效期")
        header_dict = {"Content-Type": "application/json"}
        return self.request("POST", self.OPREDIS_EXPIRE, params=param_dict)

    def opredis_config_set_req(self, param_dict):
        '''
        :param name:www1
        :param status:off
        :return:{"status":1,"result":{"www1":"off"},"errorMsg":""}
        '''
        l.info("设置开关的key和value")
        return self.request("POST", self.OPREDIS_CONFIG_SET, params=param_dict)

    def opredis_config_query_req(self, param_dict):
        '''
        :param name:www1
        :return:{"status":1,"result":{"www1":"off"},"errorMsg":""}
        '''
        l.info("获取开关的key和value")
        return self.request("GET", self.OPREDIS_CONFIG_QUERY, params=param_dict)
