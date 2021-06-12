#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests, time

from lib.util.log_util import l

RETRY_TIMES = 3
class HttpRequest(object):

    def __init__(self, host):
        self.host = host

    def get_request_with_url(self, url_path, params=None, headers=None):
        '''
        get request
        :param url_path:
        :param params:
        :param headers:
        :return:
        '''
        #url_path = "%s/%s" % (self.host, api_path)

        try:
            exheader = { 'User-Agent': 'Mobike Beta/4.3.0 (iPhone; iOS 10.2.1; Scale/2.00)'}
            if headers:
                exheader.update(headers)
            return requests.get(url=url_path, params=params, headers=exheader)
        except Exception as ex:
            l.error("get request (%s) failed, Exception:%s" % (url_path, ex))
        return None

    def get_request(self, api_path, params=None, headers=None):
        '''
        get request
        :param api_path:
        :param params:
        :param headers:
        :return:
        '''
        url_path = "%s/%s" % (self.host, api_path)
        exheader = {'User-Agent': 'Mobike Beta/4.3.0 (iPhone; iOS 10.2.1; Scale/2.00)'}
        if headers:
            exheader.update(headers)
        response = ""
        current_time = 0
        while RETRY_TIMES > current_time:
            try:
                response = requests.get(url=url_path, params=params, headers=exheader)
                if response:
                    if response.content:
                        l.debug("Response is :{0}, content:{1}".format(response, response.content))
                    else:
                        l.warn("Response is :{0}, content:{1}".format(response, response.content))

                return response
            except requests.ConnectionError as ex:
                l.warn("连接失败，重试{0}次, Exception:{1}".format(current_time+1, ex))
                if response == "":
                    time.sleep(5)
                    current_time = current_time + 1
                    continue
            except Exception as ex:
                l.error("get request (%s) failed, Exception:%s" % (url_path, ex))
                raise ex
            finally:
                if response:
                    response.close()
        #return None

    def post_request(self, api_path, params=None, headers=None, files=None, json_data=None):
        '''
        post请求
        :param api_path: api路径
        :param params: 参数列表
        :param headers: 请求头信息
        :param files: 文件上传信息
        :param json_data: json请求
        :return:
        '''
        url_path = "%s/%s" % (self.host, api_path)
        response = ""
        current_time = 0
        while RETRY_TIMES > current_time:
            try:
                response = requests.post(url=url_path, data=params, headers=headers, files=files, json=json_data)
                if response:
                    if response.content:
                        l.debug("Response is :{0}, content:{1}".format(response, response.content))
                    else:
                        l.warn("Response is :{0}, content:{1}".format(response, response.content))
                return response
            except requests.ConnectionError as ex:
                l.warn("连接失败，重试{0}次, Exception:{1}".format(current_time + 1, ex))
                if response == "":
                    time.sleep(5)
                    current_time = current_time + 1
                    continue
            except Exception as ex:
                l.error("post request (%s) failed, Exception:%s" % (url_path, ex))
                raise ex
            finally:
                if response:
                    response.close()

