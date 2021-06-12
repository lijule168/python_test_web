#!/usr/bin/env python
# -*- coding:utf-8 -*-

import types

from lib.entity.testdata_struct import TestCase, TestResult, TestResultSummary
from lib.entity.run_config import RunCaseConfig
from lib.mbmanage.dbmanage.db_model.auto_test_model import _SpiderTestCaseModel, _TestResultSummaryModel, _TestRunResultModel, _SpiderCaseTypeModel, _SpiderParentCaseTypeModel
from lib.util.log_util import l
from lib.util.time_util import TimeUtil


class CaseDBAdmin:
    all_testcases = {}

    def get_all_casedata(self):
        '''
        获取数据库中所有的测试用例
        :return:
        '''
        if CaseDBAdmin.all_testcases:
            return CaseDBAdmin.all_testcases
        __spider_testcase_model = _SpiderTestCaseModel()
        if RunCaseConfig.instance().runmode == 1:
            if RunCaseConfig().instance().run_type == 2:
                #只获取可执行测试用例
                all_cases = __spider_testcase_model.where(is_run=1).\
                    select("case_id", "test_method","test_desc", "is_run", "type_id", "owner", "request_url", "priority")
            else:
                # 获取ci且is_run为1的用例
                all_cases = __spider_testcase_model.where(is_run=1, is_ci=1). \
                    select("case_id", "test_method", "test_desc", "is_run", "type_id", "owner", "request_url",
                           "priority")
        else:
            #获取所有录入的测试用例
            all_cases = __spider_testcase_model.\
                select("case_id", "test_method", "test_desc", "is_run", "type_id", "owner", "request_url", "priority")

        CaseDBAdmin.all_testcases = self.__format_casedata(all_cases, is_new=True)
        return CaseDBAdmin.all_testcases

    def get_all_casedata_without_runmode(self):
        '''
        获取数据库中所有的测试用例
        :return:
        '''
        if CaseDBAdmin.all_testcases:
            return CaseDBAdmin.all_testcases
        __spider_testcase_model = _SpiderTestCaseModel()
        # if RunCaseConfig.instance().runmode == 1:
        #     #只获取可执行测试用例
        #     all_cases = __spider_testcase_model.where(is_run=1).\
        #         select("case_id", "test_method","test_desc", "is_run", "type_id", "owner", "request_url", "priority")
        # else:
        #获取所有录入的测试用例
        all_cases = __spider_testcase_model.\
            select("case_id", "test_method", "test_desc", "is_run", "type_id", "owner", "request_url", "priority")

        CaseDBAdmin.all_testcases = self.__format_casedata(all_cases, is_new=True)
        return CaseDBAdmin.all_testcases

    def __format_casedata(self, all_cases, is_new=False):
        all_execute_case_dict = {}
        for case_record in all_cases:
            try:
                test_case = TestCase()
                test_case.case_id = case_record[0]
                test_case.test_method = case_record[1].lower()
                test_case.test_desc = case_record[2]
                test_case.is_run = case_record[3]
                test_case.type_id = case_record[4]
                test_case.owner = case_record[5]
                test_case.request_url = case_record[6]
                test_case.priority = case_record[7]
                if is_new:
                    all_execute_case_dict[test_case.test_method] = test_case
                    continue
                test_case.http_method = case_record[8]
                test_case.request_name = case_record[9]

                if case_record[10]:
                    test_case.request_header = case_record[10]
                if case_record[11]:
                    test_case.request_param = case_record[11]

                if case_record[12]:
                    test_case.expected_result = case_record[12]
                test_case.excepted_url = case_record[13]
                test_case.handler = case_record[14]
                test_case.pre_sql = case_record[15]
                test_case.after_sql = case_record[16]
                all_execute_case_dict[test_case.test_method] = test_case
            except Exception as ex:
                l.error("测试数据赋值是失败，Message(%s)" % (ex))
        return all_execute_case_dict

    def get_all_execute_casedata(self):
         test_data_dict = self.get_all_casedata()
         return test_data_dict
         #return {k: v for k, v in test_data_dict.items() if test_data_dict[k].is_run == 1}

    def get_execute_casedata_by_caseid(self, case_ids):
        '''
        根据用例id获取用例信息
        :param case_ids: 用例list
        :return: dict, key: test_case_name
        '''
        test_data_dict = self.get_all_casedata_without_runmode()
        if not isinstance(case_ids, list):
            l.error('input params is not list, please enter again!')
            return None

        return {k: v for k, v in test_data_dict.items() if test_data_dict[k].case_id in case_ids}

    def get_execute_casedata_by_casename(self, testcase_name_filter):
        '''
        根据用例用例名获取用例数据信息（支持模块匹配）
        :param testcase_name_filter: 用例名
        :return: dict, key: 测试用例数据信息
        '''
        test_data_dict = self.get_all_casedata()
        filter = testcase_name_filter.lower()
        return {k: v for k, v in test_data_dict.items() if test_data_dict[k].test_method.__contains__(filter)}

    def get_execute_casedata_by_caselist(self, testcase_list):
        '''
        根据用例用例名获取用例数据信息（支持模块匹配）
        :param testcase_name: 用例名
        :return: dict, 测试用例集,主键:testcasename
        '''

        test_data_dict = self.get_all_casedata()
        re_dict = {}
        for item in  testcase_list:
            testcase = {k: v for k, v in test_data_dict.items() if
                test_data_dict[k].test_method.__contains__(item)}
            re_dict = dict(re_dict.items() + testcase.items())
        return re_dict

    def get_execute_casedata_by_case_owner(self, owner):
        '''
        获取某个owner下的所有用例信息
        :param owner: 用例的owner
        :return: dict, key: test_case_name
        '''
        test_data_dict = self.get_all_casedata()
        return {k: v for k, v in test_data_dict.items() if test_data_dict[k].owner.__contains__(owner)}

    def get_execute_casedata_by_typeid(self, type_ids):
        '''
        get execute case by type ids
        :param type_ids: type must be list
        :return: dict, key: test_case_name
        '''
        test_data_dict = self.get_all_casedata()
        subtypes = self.__get_subtypes_by_ptype(type_ids)
        return {k: v for k, v in test_data_dict.items() if test_data_dict[k].type_id in subtypes}

    def get_execute_casedata_by_priority(self, prioritys):
        '''
        get execute case by case priority
        :param prioritys: type must be list
        :return: dict, key: test_case_name
        '''

        test_data_dict = self.get_all_casedata()
        return {k: v for k, v in test_data_dict.items() if test_data_dict[k].priority in prioritys}

    def get_ptypeid_by_stack(self, stack_name):
        obj = _SpiderParentCaseTypeModel()
        result = obj.where(case_type=stack_name).select("id")
        if len(result) > 0:
            return result[0][0]
        return None

    def __get_subtypes_by_ptype(self, ptypes):
        sub_type = _SpiderCaseTypeModel()
        subtype_ids = sub_type.in_clause("pid in ({0}) ".format(",".join([str(key) for key in ptypes]))).select("id")
        return [key[0] for key in subtype_ids]

    def get_casetype(self, p_type, sub_type):
        '''
        根据测试类型名，获取类型id, 不存在则插入一条记录
        :param type_name:
        :return:
        '''
        casetype_model = _SpiderCaseTypeModel()
        parent_casetype_model = _SpiderParentCaseTypeModel()
        # 在父类型中查询pid
        p_items = parent_casetype_model.where(case_type=p_type).select("id")
        pid = 0
        if len(p_items)!=0:
            pid = p_items[0][0]
        # 在子类型中查询id
        items = casetype_model.where(case_type=sub_type, pid=pid).select("id")
        # 不存在子类型id则插入type
        if len(items) == 0:
            #pid不存在时，插入父类型
            if pid == 0:
                parent_casetype_model = _SpiderParentCaseTypeModel(case_type=p_type, test_type_desc="待更新")
                parent_casetype_model.save()
                p_items = parent_casetype_model.where(case_type=p_type).select("id")
                pid = p_items[0][0]
            # 插入子类型
            casetype_model = _SpiderCaseTypeModel(case_type=sub_type, test_type_desc="待更新", pid=pid)
            casetype_model.save()
            items = casetype_model.where(case_type=sub_type, pid=pid).select("id")
        return items[0][0]

    def insert_testcase(self, test_case):
        '''
        插入用例数据
        :param test_case:TestCase对象
        :return:
        '''
        if RunCaseConfig().runmode == 1:
            return
        testcase_model = _SpiderTestCaseModel()
        items = testcase_model.where(test_method=test_case.test_method).select("case_id, is_run")

        if 0 == len(items):
            testcase_model = _SpiderTestCaseModel(test_method=test_case.test_method, test_desc=test_case.test_desc,
                                                  is_run=test_case.is_run, type_id=test_case.type_id,
                                                  request_url=test_case.request_url, owner=test_case.owner,
                                                  priority=test_case.priority,
                                                  create_time=TimeUtil.format_timer_to_str())
            testcase_model.save()
        elif len(items) == 1 and items[0][1] == 0:
            testcase_model.where(test_method=test_case.test_method).update(test_method=test_case.test_method,
                                                                           test_desc=test_case.test_desc,
                                                                           is_run=test_case.is_run,
                                                                           type_id=test_case.type_id,
                                                                           request_url=test_case.request_url,
                                                                           owner=test_case.owner,
                                                                           priority=test_case.priority)
            return

    def insert_test_result(self, test_result):
        """
                save test result to db
                :param test_result: TestResult obj
                :return:
                """
        test_data = test_result.test_case
        if RunCaseConfig().runmode != 1:
            return
        if not test_result.end_time:
            test_result.end_time = TimeUtil.format_timer_to_str()
        if not test_result.start_time:
            test_result.start_time = TimeUtil.format_timer_to_str()
        obj = _TestRunResultModel()
        items = obj.where(execute_id=test_result.execute_id, case_id=test_data.case_id).select("case_id")
        if len(items) != 0:
            obj.where(execute_id=test_result.execute_id, case_id=test_data.case_id).update(
                                                    case_id=test_data.case_id,
                                                    request_url=test_data.request_url,
                                                    test_method=test_data.test_method,
                                                    test_desc=test_data.test_desc, result=test_result.result,
                                                    reason=test_result.failed_reason,
                                                    owner=test_data.owner, start_time=test_result.start_time,
                                                    end_time=test_result.end_time,
                                                    execute_time=test_result.execute_time,
                                                    execute_id=test_result.execute_id)
        else:
            __test_run_result_model = _TestRunResultModel(case_id=test_data.case_id,  request_url=test_data.request_url,
                                                      test_method=test_data.test_method,
                                                      test_desc=test_data.test_desc, result=test_result.result,
                                                      reason=test_result.failed_reason,
                                                      owner=test_data.owner, start_time=test_result.start_time,
                                                      end_time=test_result.end_time,
                                                      execute_time=test_result.execute_time,
                                                      execute_id=test_result.execute_id)
            __test_run_result_model.save()

    def insert_or_update_test_summary(self, test_result_summary):
        '''
                更新测试结果集
                :param test_summary:
                :return:
                '''
        l.info("insert test result summary to db")
        runcase_config = RunCaseConfig.instance()
        if runcase_config.runmode != 1:
            l.warn("debug模式下,不写如summary数据")
            return
        __test_result_summary_model = _TestResultSummaryModel(execute_id=test_result_summary.execute_id,
                                                              pass_count=test_result_summary.pass_count,
                                                              failed_count=test_result_summary.failed_count,
                                                              total_count=test_result_summary.failed_count + test_result_summary.pass_count,
                                                              total_execute_time=test_result_summary.total_execute_time,
                                                              start_time=test_result_summary.start_time,
                                                              end_time=test_result_summary.end_time,
                                                              dev=test_result_summary.dev,
                                                              service=test_result_summary.service,
                                                              tag=test_result_summary.tag,
                                                              env=test_result_summary.env,
                                                              type=test_result_summary.type)
        __test_result_summary_model.save()

    def query_test_result_by_execute_id(self):
        __test_run_result_model = _TestRunResultModel()
        test_results = __test_run_result_model.where(execute_id=TestResultSummary().execute_id).order_by(result=1).\
            select("case_id", "request_url", "test_method", "test_desc", "result", "reason", "owner", "execute_time")

        test_result_list = []
        for item in test_results:
            test_result = TestResult()
            test_result.test_case = TestCase()
            test_result.test_case.case_id = item[0]
            test_result.test_case.request_url = item[1]
            test_result.test_case.test_method = item[2]
            test_result.test_case.test_desc = item[3]
            test_result.execute_time = item[7]
            test_result.result = item[4]
            test_result.failed_reason = item[5]
            test_result.test_case.owner = item[6]
            test_result_list.append(test_result)

        return test_result_list



