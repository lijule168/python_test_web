#!/usr/bin/env python
import sys, os, multiprocessing
import unittest

proj_path = os.path.realpath(__file__).split('test_engine')[0]
sys.path.append(proj_path)

from optparse import OptionParser
from multiprocessing import Pool

from lib.business.case_data_business.casedata_business import CaseDataBusiness
from lib.business.env.env_business import EnvBusiness
from lib.business.env.report import HtmlReport
from lib.common.config_helper import RunConfig
from lib.entity.run_config import RunCaseConfig
from lib.entity.testdata_struct import TestResultSummary, TestResult
from lib.util.email_util import send_email
from lib.util.log_util import l
from lib.util.time_util import TimeUtil
from lib.util.path_util import *

execute_id = int(TimeUtil.get_timestamp() / 1000)
casedata_business = CaseDataBusiness()

def run(execute_testcases, sub_dir=""):
    test_suite = create_suite(execute_testcases, sub_dir)
    # test_suite = create_suite_for_all(sub_dir)
    if test_suite.countTestCases() == 0:
        return
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)

    if RunCaseConfig.instance().runmode != 1:
        return

    for error_item in result.errors:
        test_result = TestResult()
        test_result.execute_id = TestResultSummary().execute_id
        try:
            test_result.test_case = execute_testcases[error_item[0]._testMethodName.lower()]
            test_result.result = "Fail"
            test_result.failed_reason = error_item[1]
            casedata_business.insert_test_result(test_result)
        except Exception as e:
            l.error(error_item)
            l.error("添加结果失败：{0}".format(e))

def create_suite(execute_testcases, sub_dir=""):
    '''
    create test suite
    :param execute_testcases:
    :return: None
    '''
    test_suite = unittest.TestSuite()
    path = "%s/script/api_test/%s" % (proj_path, sub_dir)
    discover = unittest.defaultTestLoader.discover(path, pattern='test_*.py')
    for suite in discover:
        for case in suite:
            for c in case:
                if c._testMethodName.lower() in execute_testcases:
                    l.info(c._testMethodName)
                    test_suite.addTest(c)
    return test_suite

def multi_run(execute_testcases):
    # global execute_id
    pool = Pool(processes=multiprocessing.cpu_count() * 4)
    sub_dirs = get_sub_dirs(proj_path + "/script/api_test")
    for sub_dir in sub_dirs:
        pool.apply_async(run, args=(execute_testcases, sub_dir, execute_id,))
    pool.close()
    pool.join()


def for_debug():
    # RunCaseConfig.instance().runmode = 1
    RunCaseConfig.instance().case_ids = [166, 167]
    RunCaseConfig.instance().case_type_ids = [32]

    RunCaseConfig.instance().env = 'banana'
    run_mode = 5
    case_ids = [134]
    testcase_name = 'test_get_prainfo'

    owner = 'wangsong'
    test_case_dict = {}
    # 执行所有测试用例
    if 1 == run_mode:
        test_case_dict = casedata_business.get_all_execute_casedata()
    # 跑输入的所有属于用例类型的测试用例
    elif 2 == run_mode:
        case_type_ids = [2]  # RunCaseConfig.instance().case_type_ids
        test_case_dict = casedata_business.get_execute_casedata_by_typeid(case_type_ids)
    # 跑输入id所有相关的测试用例
    elif 3 == run_mode:
        case_ids = case_ids  # RunCaseConfig.instance().case_ids
        test_case_dict = casedata_business.get_execute_casedata_by_caseid(case_ids)
    elif 4 == run_mode:
        test_case_dict = casedata_business.get_execute_casedata_by_case_owner(owner)
    # 跑指定的测试用例(支持模糊匹配)
    elif 0 == run_mode:
        test_case_dict = casedata_business.get_execute_casedata_by_casename(testcase_name)
    elif 5 == run_mode:
        test_case_dict = {testcase_name.lower(): testcase_name}

    return test_case_dict


def get_optionparser():
    parse = OptionParser()
    parse.add_option("-e", "--env", type="string", dest="env", help="被测的环境名")
    parse.add_option("-s", "--service", type="string", dest="service", help="被测的服务名")
    parse.add_option("-n", "--tag_num", type="string", dest="tag_num", help="被测服务的版本号")
    parse.add_option("-d", "--deployer", type="string", dest="deployer", help="打包人员邮件地址")
    parse.add_option("-t", "--typeid", type="string", dest="typeids",
                     help="测试用例类型，从autotest.case_type中获取, ex: --type=1,2")
    parse.add_option("--stack", type="string", dest="stack_name",
                     help="stack名称")
    parse.add_option("-p", "--priority", type="string", dest="prioritys", help="测试用例优先级, ex: --priority=1,2 ")
    parse.add_option("--caseid", type="string", dest="case_ids", help="测试用例ID集 , ex: --ids=1,2,3")
    parse.add_option("--reportid", type="string", dest="reportid", help="标识用例执行的唯一ID, 类型为整形")
    parse.add_option("--type", type="string", dest="run_type", help="-1表示跑门禁测试中添加组合条件，0表示门禁测试（is_ci=1，优先级为1，2），"
                                                                    "1表示ci全量测试(is_ci=1的所有用例), 2表示is_run为1的组合用例")
    parse.add_option("--emails", type="string", dest="receiver_list", help="收件人邮件列表")
    parse.add_option("--email_subject", type="string", dest="email_subject", help="email主题")
    return parse


def strlist_to_intlist(str_list):
    int_list = []
    for item in str_list:
        try:
            int_list.append(int(item.strip()))
        except Exception as ex:
            raise Exception("{0}, item is {1}, 不能转化为int类型, allitem:{2}".format(ex, item, str_list))
    return int_list


if __name__ == '__main__':
    start_time = TimeUtil.get_timestamp() / 1000
    run_config = RunConfig()
    test_result_summary = TestResultSummary()
    test_result_summary.execute_id = execute_id
    if len(sys.argv) < 2:
        # for debug
        test_case_dict = for_debug()
        run(test_case_dict, sub_dir="")
        # multi_run(test_case_dict)
    else:
        # 删除日志文件
        if os.path.isfile("api_auto_test_debug.log"):
            with open("api_auto_test_debug.log", "wb") as file:
                pass

        parser = get_optionparser()
        options, args = parser.parse_args(sys.argv)

        if options.env is None:
            env = 'standford'
        else:
            env = options.env
        service = options.service
        if service is None:
            service = ""
        tag_num = options.tag_num
        if tag_num is None:
            tag_num = "0.0.0"
        deployer = options.deployer
        if deployer is None:
            deployer = "dingbaixia@mobike.com"
        report_id = options.reportid
        prioritys = options.prioritys
        # 跑所有可执行的测试用例
        types = options.typeids
        stack = options.stack_name
        ids = options.case_ids
        if options.run_type is None:
            run_type = -1
        else:
            run_type = int(options.run_type.strip())
            if run_type == 0:
                prioritys = "0,1,2"
                types = None
                ids = None
            elif run_type == 1:
                prioritys = None
                types = None
                ids = None

        RunCaseConfig.instance().run_type = run_type
        test_result_summary.type = run_type

        if report_id is not None:
            try:
                test_result_summary.execute_id = int(report_id.strip())
            except Exception as ex:
                l.error(ex)
                raise Exception("{0}, reportid is {1}, 不能转化为int类型".format(ex, report_id))
        else:
            test_result_summary.execute_id = execute_id
        if env:
            RunCaseConfig.instance().env = env
        test_result_summary.env = env
        test_result_summary.dev = deployer
        test_result_summary.service = service
        RunCaseConfig.instance().runmode = 1
        test_result_summary.tag = tag_num

        test_case_dict = {}
        receiver_list = []
        try:
            if stack:
                pid = casedata_business.get_ptypeid_by_stack(stack_name=stack)
                if pid:
                    types = "{0}".format(pid)
            if types:
                type_ids = types.split(',')
                test_case_dict = casedata_business.get_execute_casedata_by_typeid(
                    type_ids=strlist_to_intlist(type_ids))
            if prioritys:
                priority_ids = prioritys.split(',')
                test_case_dict_p = casedata_business.get_execute_casedata_by_priority(
                    prioritys=strlist_to_intlist(priority_ids))
                if test_case_dict:
                    test_case_dict = dict.fromkeys([key for key in test_case_dict if key in test_case_dict_p])
                    for key in test_case_dict.keys():
                        test_case_dict[key] = test_case_dict_p[key]

                else:
                    test_case_dict = test_case_dict_p
            if ids:
                case_ids = ids.split(',')
                test_case_dict_id = casedata_business.get_execute_casedata_by_caseid(
                    case_ids=strlist_to_intlist(case_ids))
                if test_case_dict:
                    test_case_dict = dict.fromkeys([key for key in test_case_dict_id if key in test_case_dict])
                    for key in test_case_dict.keys():
                        test_case_dict[key] = test_case_dict_id[key]
                else:
                    test_case_dict = test_case_dict_id
            if not test_case_dict:
                # 没有传入type，priority, caseid,则执行所有用例
                test_case_dict = casedata_business.get_all_execute_casedata()
            # multi_run(test_case_dict)
            run(test_case_dict)
            test_results = casedata_business.query_test_result_by_execute_id()
            failed_case_list = [item for item in test_results if item.result == "Fail"]
            if failed_case_list.__len__() > 0:
                failed_case_dict = {}
                for item in failed_case_list:
                    failed_case_dict[item.test_case.test_method.lower()] = test_case_dict[item.test_case.test_method.lower()]
                run(failed_case_dict)
            end_time = TimeUtil.get_timestamp() / 1000
            test_results = casedata_business.query_test_result_by_execute_id()

            for item in test_results:
                if item.result == "Pass":
                    test_result_summary.pass_count = test_result_summary.pass_count + 1
                else:
                    test_result_summary.failed_count = test_result_summary.failed_count + 1
                    test_result_summary.failed_case_list.append(item.test_case.test_method)
            l.info(
                "================================================Summary================================================")
            l.info("执行%s条用例，Pass:%s Fail:%s" % (test_result_summary.pass_count + test_result_summary.failed_count,
                                                test_result_summary.pass_count, test_result_summary.failed_count))
            l.info("失败的用例：%s" % ",".join(test_result_summary.failed_case_list))

            if RunCaseConfig.instance().runmode == 1:
                test_result_summary.start_time = TimeUtil.format_timer_to_str(start_time)
                test_result_summary.end_time = TimeUtil.format_timer_to_str(end_time)
                test_result_summary.total_execute_time = end_time - start_time
                casedata_business.update_test_summary(test_result_summary)

                html_report = HtmlReport()
                html_report.generate_html('test report', '{0}/report/report_{1}.html'.format(proj_path,
                                                                                             test_result_summary.execute_id))
                title = "测试结果"
                if run_type == 1:
                    title = "全量自动化测试报告"
                elif run_type == 0:
                    title = "门禁自动化测试报告"
                elif run_type == 2:
                    title = "自动化测试报告"
                if options.email_subject:
                    title = options.email_subject

                receivers = options.receiver_list
                if receivers:
                    receiver_list = receiver_list + receivers.split(',')
                if test_result_summary.dev and test_result_summary.dev.__contains__('@mobike.com'):
                    receiver_list = receiver_list + test_result_summary.dev.split(',')
                send_email(html_report.email_content(), receiver_list, title)
        except Exception as ex:
            l.error('system exception, {0}'.format(ex))
            content = str(ex)
            title = "系统异常"
            receivers = options.receiver_list
            if receivers:
                receiver_list = receiver_list + receivers.split(',')
            if test_result_summary.dev and test_result_summary.dev.__contains__('@mobike.com'):
                receiver_list = receiver_list + test_result_summary.dev.split(',')
            send_email(content, receiver_list, title)
        finally:
            EnvBusiness.clean_env()