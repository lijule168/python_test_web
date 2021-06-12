#!/usr/bin/python
#-*- coding:utf-8 -*-
from lib.common.decorate import Decorate

__author__ = 'dingbaixia'

from lib.util.log_util import l
from lib.common.config_helper import EnvConfig
from lib.common.http_helper import HttpRequest
from lib.mbmanage.microservice_manage.microservcie_manage import MicroServiceManage

class BaseReq(object):
    host = None
    def __init__(self, micro_service_name=None):
        if micro_service_name:
            self.host = self.__get_microservice_host(micro_service_name)
        self.api_host = EnvConfig().mobike_http_service.mobike_api_host
        self.athena_host = EnvConfig().mobike_http_service.athena_host
        self.mercury_host = EnvConfig().mobike_http_service.mercury_host
        self.mola_host = EnvConfig().mobike_http_service.mola_host

    def __get_microservice_host(self, micro_service_name):
        '''
        获取微服务的host信息
        :param micro_service_name: 微服务的名称
        :return:
        '''
        return MicroServiceManage.get_domain(micro_service_name=micro_service_name)

    @Decorate.request_decorate
    def request(self, http_method, api_path, params=None, headers=None, files=None, json_data=None):
        response = None
        try:
            if self.host:
                self.__req = HttpRequest(self.host)
            elif api_path.startswith('athena'):
                self.__req = HttpRequest(self.athena_host)

                if http_method == "POST" and json_data != None:
                    api_path = api_path + "?" + "LOGIN_ID=limin&userPasswd=m0bike123456"
                else:
                    if params is None:
                        params = {}
                    params["LOGIN_ID"] = 'limin'
                    params["userPasswd"] = 'm0bike123456'
            elif api_path.startswith('mercury'):
                self.__req = HttpRequest(self.mercury_host)

                if http_method == "POST" and json_data != None:
                    api_path = api_path + "?" + "LOGIN_ID=limin&userPasswd=m0bike123456"
                else:
                    if params is None:
                        params = {}
                    params["LOGIN_ID"] = 'limin'
                    params["userPasswd"] = 'm0bike123456'
            elif api_path.startswith("mola"):
                self.__req = HttpRequest(self.mola_host)
            elif api_path.startswith('mobike-api'):
                self.__req = HttpRequest(self.api_host)
            elif api_path.startswith('api/'):
                self.__req = HttpRequest(self.api_host)
            else:
                l.warn("还不认识此服务请求，请添加")
            l.info("发送请求：method:{0}, host:{6} api_path:{1}, header:{2}, params:{3}, json_data:{4}, files:{5}".format (
                http_method, api_path, headers, params, json_data, files, self.__req.host))
            method_upper = http_method.upper()
            if method_upper == 'GET':
                response = self.__req.get_request(api_path=api_path, params=params, headers=headers)
            elif method_upper == 'POST':
                if headers:
                    if not "User-Agent" in headers:
                        headers["User-Agent"] ="Mobike/6.9.0 (iPhone; iOS 10.2.1; Scale/3.00)"
                else:
                    headers = {}
                    headers["User-Agent"] = "Mobike/6.9.0 (iPhone; iOS 10.2.1; Scale/3.00)"
                if json_data:
                    headers["Content-Type"] = "application/json"

                response = self.__req.post_request(api_path=api_path, params=params, headers=headers, files=files, json_data=json_data)
            else:
                l.warn('暂不支持此类请求(%s)' % http_method)
            try:
                response = response.json()
            except Exception as ex:
                l.warn("json解析失败，直接返回response(%s)" % response.content)
                return response
                #raise ex
        except Exception as ex:
            l.error('请求失败, error message:%s' % ex)
            #response = None
            raise ex
        return response

    def _format_jsonreq_path(self, param_dict={}):
        params = ""
        for (key, item) in param_dict.items():
            params = params + key + "=" + str(item) +"&"
        if params:
            params = params[0:len(params)-1]
        return params