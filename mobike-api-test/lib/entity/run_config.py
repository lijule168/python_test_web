#!/usr/bin/env python
# -*- coding:utf-8 -*-
class RunCaseConfig(object):
    '''
    run用例的配置参数
    '''
    env = ""
    runmode = 1
    # debug_mode = 0
    case_ids = []
    case_type_ids = {"25": []}
    run_type = 0
    # start_time = None
    # end_time = None
    # execute_id = 0
    # execute_duration = 0
    # failed_case_count = 0
    # pass_case_count = 0
    # deployers = ""
    # version = ""
    # pass_case_list = []
    # failed_case_list = []
    receiver_list = []

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(RunCaseConfig, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    @staticmethod
    def instance():
        return RunCaseConfig()

class RunCaseUserConfig:
    '''
    run用例使用的数据
    '''
    run_one_user = 0
    run_user_mobileNo = '15650761520'

class EmailConfig:
    server = "smtp.partner.outlook.cn"
    port = 587
    sender = "automation@mobike.com"
    passwd = "ABC.1234"
    recevier = []