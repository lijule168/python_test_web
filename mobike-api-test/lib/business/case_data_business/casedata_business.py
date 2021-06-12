#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib.util.log_util import l
from lib.mbmanage.dbmanage.casedb_admin import CaseDBAdmin

class CaseDataBusiness(object):
    def __init__(self):
        self.casedb_admin = CaseDBAdmin()

    def get_execute_casedata_by_caseid(self, case_ids):
        '''
        根据用例id获取用例信息
        :param case_ids:用例list
        :return: dict, 测试用例集,主键:testcasename
        '''
        if not isinstance(case_ids, list):
            l.error('input params is not list, please enter again!')
            return None
        return self.casedb_admin.get_execute_casedata_by_caseid(case_ids=case_ids)

    def get_all_execute_casedata(self):
        '''
        获取所有可执行用例
        :return:
        '''
        return  self.casedb_admin.get_all_execute_casedata()

    def get_execute_casedata_by_casename(self, testcase_name):
        '''
        根据用例用例名获取用例数据信息（支持模块匹配）
        :param testcase_name: 用例名
        :return: dict, 测试用例集,主键:testcasename
        '''
        return self.casedb_admin.get_execute_casedata_by_casename(testcase_name_filter=testcase_name)

    def get_execute_casedata_by_caselist(self, testcase_list):
        '''
        根据用例用例名获取用例数据信息（支持模块匹配）
        :param testcase_name: 用例名
        :return: dict, 测试用例集,主键:testcasename
        '''
        return self.casedb_admin.get_execute_casedata_by_caselist(testcase_list=testcase_list)

    def get_execute_casedata_by_case_owner(self, owner):
        '''
        获取某个owner下的所有用例信息
        :param owner: 用例的owner
        :return: dict, 测试用例集,主键:testcasename
        '''
        return self.casedb_admin.get_execute_casedata_by_case_owner(owner=owner)

    def get_execute_casedata_by_typeid(self, type_ids):
        '''
        get execute case by type ids
        :param type_ids: type must be list
        :return: dict, 测试用例集,主键:testcasename
        '''
        if not isinstance(type_ids, list):
            l.error('input params(type_ids) is not list, please enter again!')
            return None
        return self.casedb_admin.get_execute_casedata_by_typeid(type_ids=type_ids)

    def get_execute_casedata_by_priority(self, prioritys):
        '''
        get execute case by case priority
        :param prioritys: type must be list
        :return: dict, 测试用例集,主键:testcasename
        '''
        if not isinstance(prioritys, list):
            l.error('input params(type_ids) is not list, please enter again!')
            return None
        return self.casedb_admin.get_execute_casedata_by_priority(prioritys=prioritys)

    def insert_test_result(self, test_result):
        '''
        save test result to db
        :param test_result: TestResult obj
        :return:
        '''
        l.info("insert testresult to db")
        self.casedb_admin.insert_test_result(test_result)

    def query_test_result_by_execute_id(self):
        '''
        根据execute_id获取测试结果数据
        :return:
        '''
        return self.casedb_admin.query_test_result_by_execute_id()

    def update_test_summary(self, test_result_summary):
        '''
        更新测试结果集
        :param test_result_summary:
        :return:
        '''
        return self.casedb_admin.insert_or_update_test_summary(test_result_summary)

    def get_casetypeid(self, p_type=None, sub_type=None):
        '''
        根据测试类型名，获取类型id, 不存在则插入一条记录
        :param type_name:
        :return:
        '''
        return self.casedb_admin.get_casetype(p_type, sub_type)

    def insert_testcase_todb(self, test_case):
        '''
        插入用例数据
        :param test_case:TestCase对象
        :return:
        '''
        return self.casedb_admin.insert_testcase(test_case)

    def get_ptypeid_by_stack(self, stack_name):
        return self.casedb_admin.get_ptypeid_by_stack(stack_name)