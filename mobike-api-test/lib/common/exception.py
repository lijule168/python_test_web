# -*- coding:utf-8 -*-

class ApiException(Exception):
    """ Common base class for all non-exit exceptions. """

    def __init__(self, api_name, msg):  # real signature unknown
        Exception.__init__(self, "接口({0})请求错误：".format(api_name) + msg)

class ServiceException(Exception):
    """ Common base class for all non-exit exceptions. """

    def __init__(self,service_name, msg):  # real signature unknown
        Exception.__init__(self, "服务({0})错误：".format(service_name) + msg)

class DBException(Exception):
    def __init__(self, db_name, msg):
        Exception.__init__(self, "数据库({0})错误:".format(db_name) + msg)

class RedisException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, "Redis错误：" + msg)