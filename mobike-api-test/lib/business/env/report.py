#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import sys
import time
import json

from lib.mbmanage.dbmanage.casedb_admin import CaseDBAdmin
from lib.entity.testdata_struct import TestResultSummary
from lib.ref.pyh import *
from lib.util.log_util import l

class HtmlReport:
    def __init__(self):
        self.title = 'test_report_page'   # 网页标签名称
        self.filename = ''                   # 结果文件名
        self.success_num = 0                  # 测试通过的用例数
        self.fail_num = 0                     # 测试失败的用例数
        self.error_num = 0                    # 运行出错的用例数
        self.case_total = 0                   # 运行测试用例总数

    # 生成HTML报告
    def generate_html(self, head, file):
        test_result_summary = TestResultSummary()
        page = PyH(self.title)
        page << h1(head, align='center') # 标题居中

        page << p('测试总耗时：%s' % test_result_summary.total_execute_time)

        test_result_list = CaseDBAdmin().query_test_result_by_execute_id()
        self.case_total = test_result_list.__len__()
        self.fail_num = test_result_summary.failed_count
        self.success_num = test_result_summary.pass_count

        page << p('测试用例数：' + str(self.case_total) + '&nbsp'*10 + '成功用例数：' + str(self.success_num) +
                  '&nbsp'*10 + '失败用例数：' + str(self.fail_num) + '&nbsp'*10)
        #  表格标题caption 表格边框border 单元边沿与其内容之间的空白cellpadding 单元格之间间隔为cellspacing

        tab = table( border='1', cellpadding='1', cellspacing='0', cl='table')
        tab1 = page << tab
        tab1 << tr(td('用例ID', bgcolor='#ABABAB', align='center')
                   + td('HTTP方法', bgcolor='#ABABAB', align='center')
                   + td('接口名称', bgcolor='#ABABAB', align='center')
                   + td('请求URL', bgcolor='#ABABAB', align='center')
                   + td('请求参数/数据', bgcolor='#ABABAB', align='center')
                   + td('测试方法', bgcolor='#ABABAB', align='center')
                   + td('测试描述', bgcolor='#ABABAB', align='center')
                   + td('测试结果', bgcolor='#ABABAB', align='center')
                   + td('失败原因', bgcolor='#ABABAB', align='center'))

        for test_result in test_result_list:
            tab1<< tr(td(int(test_result.test_case.case_id)) + td(test_result.test_case.http_method) +
                          td(test_result.test_case.request_name) + td(test_result.test_case.request_url) +
                          td(test_result.test_case.request_param) + td(test_result.test_case.test_method) + td(test_result.test_case.test_desc) +
                          td(test_result.result) + td(test_result.failed_reason))

        #self.__set_result_filename(file)
        page.printOut(file)

    def email_content(self):
        flag = "Error"
        pass_cnt = 0
        fail_cnt = 0
        pass_rate = 0.0
        result_list = []
        test_result = "Fail"
        td1 = ''
        tr1 = ''
        summary_dict = {}

        test_result_summary = TestResultSummary()
        end_time = test_result_summary.end_time

        # test_version = test_result_summary.env + "_" + test_result_summary.service + "@" + test_result_summary.tag
        test_version = test_result_summary.env + "_" + test_result_summary.service
        deployer_name = test_result_summary.dev
        try:
            test_result_list = CaseDBAdmin().query_test_result_by_execute_id()
            total_case = len(test_result_list)
            title = 'Test Result : %s' % (total_case)
            str_rate = 0
            pass_cnt = test_result_summary.pass_count
            fail_cnt = test_result_summary.failed_count
            if total_case != 0:
                pass_rate = round(pass_cnt / float(total_case), 2)
                str_rate = format(pass_rate, '.2%')
            if fail_cnt >= 1:
                test_result = "Fail"
            else:
                test_result = "Pass"

            summary_dict["Passed"] = test_result_summary.pass_count
            summary_dict["Failed"] = test_result_summary.failed_count
            summary_dict["Rate"] = str_rate
            summary_dict["Result"] = test_result
            summary_dict["Deployer"] = test_result_summary.dev
            summary_dict["Start_time"] = test_result_summary.start_time
            summary_dict["End_time"] = test_result_summary.end_time
            summary_dict["Duration"] = int(test_result_summary.total_execute_time)
            # summary_dict["Tag"] = test_result_summary.tag
            summary_dict["Service"] = test_result_summary.service
            summary_dict["Env"] = test_result_summary.env

            with open('../report/report_%s.json' % test_result_summary.execute_id, 'w') as json_file:
                json_file.write(json.dumps(summary_dict))

            header = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head>'
            th1 = '<body text="#000000"><center>Automation Test Report <font color="#ff0000"><b></b></font></center>' \
                  '<br/><left>1、Test Summary: <font color = "#dd0000"><b></b></font></left>' \
                  '<br/>' \
                  '<table border="1" cellspacing="0" cellpadding="3" bordercolor="#000000" width="80%" align="center" >' \
                  '<tr bgcolor="#F79646" align="left" >' \
                  '<th>test_version</th><th>Start_Time</th><th>End_Time</th><th>total_case</th><th>Passed</th><th>Failed</th><th>Rate</th><th>Result</th>' \
                  '<th>Deployer</th> ' \
                  '</tr>'
            td1 += '<td>' + test_version + '</td>' + '<td>' + str(summary_dict["Start_time"]) + '</td>' \
                   + '<td>' + str(summary_dict["End_time"]) + '</td>' + '<td>' + str(
                total_case) + '</td>' + '<td>' + str(pass_cnt) + '</td>'
            td1 += '<td>' + str(
                fail_cnt) + '</td>' + '<td>' + str(str_rate) + '</td>' + '<td>' + test_result + '</td>' + '<td>' + deployer_name + '</td>'
            tr1 += '<tr>' + td1 + '</tr>'
            tr1 = tr1.encode('utf-8')
            tb1_end = '</table>'

            th2_title = '<br/><left>2、Test Details: <font color = "#dd0000"><b></b></font></left>'
            th2 = '<br/><table border="1" cellspacing="0" cellpadding="3" bordercolor="#000000" width="80%" align="center" >' \
                  '<tr style="background-color:#F79646" align="left"><th>case_id</th><th>request_url</th>' \
                  '<th>test_desc</th><th>result</th><th>reason</th><th>execute_time(s)</th><th>owner</th>' \
                  '</tr>'
            tr = ''
            for item in test_result_list:

                td = ''
                td = td + '<td>' + str(item.test_case.case_id) + '</td>'
                td = td + '<td>' + item.test_case.test_method + '</td>'
                td = td + '<td>' + item.test_case.test_desc + '</td>'
                td = td + '<td>' + item.result + '</td>'
                td = td + '<td>' + item.failed_reason + '</td>'
                td = td + '<td>' + str(item.execute_time/1000.0) + '</td>'
                td = td + '<td>' + item.test_case.owner + '</td>'
                if item.result == 'Fail':
                    tr = tr + '<tr style="background-color:#FF95CA">' + td + '</tr>'
                else:
                    tr = tr + '<tr>' + td + '</tr>'
            #tr = tr#.encode('utf-8')
            body = tr
            tail = '</table></body></html>'
            # 将内容拼接成完整的HTML文档
            mail = str(header) + str(th1) + str(tr1) + str(tb1_end) + str(th2_title) + str(th2) + str(body) + str(tail)
            return mail
        except Exception as e:
            l.info("Error: unable to fecth data {0}".format(e))
            flag = e
        return flag

    # 设置结果文件名

    def __set_result_filename(self, filename):
        self.filename = filename
        #判断是否为目录
        if os.path.isdir(self.filename):
            raise IOError("%s must point to a file" % filename)
        elif '' == self.filename:
            raise IOError('filename can not be empty')
        else:
            parent_path, ext = os.path.splitext(filename)
            tm = time.strftime('%Y%m%d%H%M%S', time.localtime())
            self.filename = parent_path + tm + ext

