#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time, threading

Lock = threading.Lock()


class CaseFilterType:
    """
    用例过滤类型
    """
    NO_FILTER = 1 #无过滤
    CASE_ID_FITER = 2 #用例ID
    CASE_TYPE_FILTER = 4 #用例类型
    CASE_PRIORITY_FILTER = 8 #用例优先级
    CASE_NAME_FILTER = 16 #用例名字过滤


class TestCase:
    """
    于接收读取的测试数据,记录要写入测试报告的数据
    """

    def __init__(self):
        self.case_id = 0  # 用例ID
        self.http_method = ''  # 接口http方法
        self.request_name = ''  # 接口ming
        self.request_url = ''  # 接口请求url
        self.request_header = ''
        self.request_param = ''# 请求参数
        self.test_method = ''  # 测试方法
        self.test_desc = ''  # 测试(用力)描述
        self.result = ''  # 测试结果
        self.reason = ''  # 失败原因
        self.expected_result = ''  # 预期结果
        self.expected_result_by_Dynamic = ''#动态获取预期结果
        self.pre_sql = '' #数据准备sql
        self.after_sql = ''
        self.owner = ''# case owner
        self.is_run = 0
        self.type_id = 0
        self.excepted_url = ''
        self.handler = ''
        self.redis_cmd = ''
        self.priority = 1
        self.is_ci = 0

    def __str__(self):
        return "method(%s), request_header(%s), request_params(%s), excepted_result(%s)" % (self.test_method,
            self.request_header, self.request_param, self.expected_result)


class TestResult:
    """
    每条测试结果对象
    """
    test_case = TestCase()
    execute_id = ''
    start_time = ''
    end_time = ''
    execute_time = 0
    result = ''
    failed_reason = ''


class TestResultSummary(object):
    """
    测试结果
    """
    execute_id = int(time.time())
    pass_count = 0
    failed_count = 0
    start_time = ''
    end_time = ''
    total_execute_time = 0
    dev = ''
    service = ''
    tag = ''
    pass_case_list = []
    failed_case_list = []
    env = ""
    type = None

    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            try:
                Lock.acquire()
                if not cls.__instance:
                    cls.__instance = super(TestResultSummary, cls).__new__(cls, *args, **kwargs)
            finally:
                Lock.release()
        return cls.__instance

    def __str__(self):
        return "execute_id(%s), pass_count(%s), failed_count(%s), start_time(%s), end_time(%s)," \
               "total_execute_time(%s), dev(%s), service(%s), tag(%s), env(%s), type(%s)" % \
               (self.execute_id, self.pass_count, self.failed_count, self.start_time, self.end_time,
                self.total_execute_time, self.dev, self.service, self.tag, self.env, self.type)

    @staticmethod
    def instance():
        return TestResultSummary()

class TestKey:
    """
    用于参数化用例数据
    """
    ACCESS_TOKEN = "authtoken"
    USER_ID = "userid"
    MOBILE_NUM = "mobileno"
    USER_RSACODE = "rsacode"
    USER_DEPOSIT = "deposit"
    CITY_CODE = "city_code"
    COUNTRY_CODE = "country"
    SOURCE = "source"
    TOTP_BIKE_ID = "totp_bike_id"
    COMMON_BIKE_ID = 'bike_id'
    USER_NAME = "username"
