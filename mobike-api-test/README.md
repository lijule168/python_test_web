# 1. 目的
### 摩拜接口，业务自动化框架。提供简单易用的用例编写方式。
# 2. 环境包安装
 - 1、安装依赖包
    pip install -r requirements.txt
 - 2、python连接mysql
    https://dev.mysql.com/downloads/connector/python/
 - 3、安装MySQLdb
    http://www.codegood.com/downloads
# 3. 代码结构
## 3.1 主要代码清单
 - test_engine\main.py 用例执行入口
 - config 环境配置文件
 - script 用例脚本
 - lib 框架库
    - business 用例业务层：请求，redis，DB，mongodb层的封装
    - mbmanage 管理层：http,grpc,redis, db,mongodb管理层
    - entity 业务实体类：框架内部实体类
    - util 框架封装的常用公共方法
    -- common 框架核心基础类：orm, http, mongodb, mysql, redis
 - tools 框架辅助工具
    - tools/gencode/gen_dbmodel.py 数据库映射生成工具
    - tools/gencode/gen_sourcecode.py api用例生成工具

# 4. 编写接口用例（以trialperiod微服务的userTrialQualification接口为例）
## 4.1 创建req文件
   - 创建目录，目录名为服务名称，在lib/mbmanage/requestmanage下创建
   - 创建请求文件：接口所在的文件名（去除mbk,control字符）加上"_req"作为文件名
   - 添加接口代码：
        ```#!/usr/bin/python
        # -*- coding:utf-8 -*-
        from lib.entity.microservice_name import MicroServiceName
        from lib.mbmanage.requestmanage.base_req import BaseReq
        class TrialPeriodReq(BaseReq):
            def __init__(self):
                super(TrialPeriodReq, self).__init__(micro_service_name=MicroServiceName.TRIALPERIOD)
            def usertrialqualification(self , param_dict=None):
                return self.request("POST", "trialperiod/check/userTrialQualification", params=param_dict)
                
## 4.2 创建business文件
   - 创建目录， 目录名称为服务名称，在lib/business下创建
   - 创建业务文件，文件名为接口所属的文件名（去除mbk, control字符）加上"_business"作为文件名
   - 添加测试业务代码：
        ```#!/usr/bin/python
        # -*- coding:utf-8 -*-
        import datetime
        from lib.business.base_business import BaseBusiness
        from lib.business.mysqldb.mbk_activity_db_business import MBKTrailRecordsTBBusiness
        from lib.entity.db_entity.mbk_activity import MBK_Tial_Records
        from lib.mbmanage.redismanage.codis_manage import CodisManage
        from lib.mbmanage.requestmanage.trialperiod.trialperiod_req import TrialPeriodReq, TrialPeriodApiReq
        from lib.mbmanage.dbmanage.mbk_activity_admin import MBKTrailRecordsTable
        class TrialPeriodBusiness(BaseBusiness):
            def __init__(self):
                super(TrialPeriodBusiness, self).__init__()
                self.__instance = TrialPeriodReq()
                self.__api_instance = TrialPeriodApiReq()
                self.__trail_records = MBKTrailRecordsTBBusiness()
        
            def usertrialqualification(self, userId=None):
                header_dict, param_dict, file_dict = self.init_params(locals().copy())
                response = self.__instance.usertrialqualification(param_dict=param_dict)
                return response
## 4.3 创建脚本文件
   - 创建脚本所在目录，以服务名为父目录，接口所属文件（去除mbk,control）为子目录，在script/api_test下创建
   - 创建脚本文件，格式：test_接口名.py，为了避免重复，建议加上服务名，如test_服务名_接口名.py
   - 添加脚本代码
        ```#!/usr/bin/python
        # -*- coding:utf-8 -*-
        from lib.entity.testdata_struct import TestKey
        from lib.util.random_util import RandomUtil
        from script.base_testcase import BaseTestCase
        from script.assert_util import AssertUtil
        from lib.business.trialperiod.trialperiod_business import TrialPeriodBusiness
        **#加上脚本的所有者**
        __author__ = "yuanyongsheng@mobike.com"
        class TestuserTrialQualification(BaseTestCase):
            def setUp(self):
                pass
            def tearDown(self):
                pass
            **#在脚本上方加上装饰器**
            @BaseTestCase.case_decorate(priority=2, is_run=0, request_url="trialperiod/check/userTrialQualification", desc="检验新用户是否有资格试骑-新用户没有试骑资格")
            def test_usertrialqualification_001(self):
                pass

# 5. 用例执行
## 5.1 调试用例
 - 设置调试环境
 RunCaseConfig.instance().env = 'guru'
 - 设置调试模式
 run_mode = 0
 - 详细配置代码：
    ```
    def for_debug():
    #RunCaseConfig.instance().runmode = 1
    RunCaseConfig.instance().case_ids = [166, 167]
    RunCaseConfig.instance().case_type_ids = [32]
    #设置调试环境
    RunCaseConfig.instance().env = 'guru'
    #设置运行模式
    run_mode = 3
    case_ids = [146]
    testcase_name = 'test_gaea_insertredpacketwater_001'

    owner = 'wangsong'
    test_case_dict={}
    #执行所有测试用例
    if 1 == run_mode:
        test_case_dict = casedata_business.get_all_execute_casedata()
    # 跑输入的所有属于用例类型的测试用例
    elif 2 == run_mode:
        case_type_ids = [2]#RunCaseConfig.instance().case_type_ids
        test_case_dict = casedata_business.get_execute_casedata_by_typeid(case_type_ids)
    # 跑输入id所有相关的测试用例
    elif 3 == run_mode:
        case_ids = case_ids#RunCaseConfig.instance().case_ids
        test_case_dict = casedata_business.get_execute_casedata_by_caseid(case_ids)
    elif 4 == run_mode:
        test_case_dict = casedata_business.get_execute_casedata_by_case_owner(owner)
    # 跑指定的测试用例(支持模糊匹配)
    elif 0 == run_mode:
        test_case_dict = casedata_business.get_execute_casedata_by_casename(testcase_name)
    elif 5 == run_mode:
        test_case_dict = {testcase_name.lower(): testcase_name}

    return test_case_dict
## 5.2 执行用例
 - 按优先级运行  python main.py --env=brave --deployer=dingbaixia@mobike.com --service=gaea --tag_num=1.0.0 --priority=1,2 --reportid=xxx 
 - 按测试用例类型运行 python main.py --env=brave --deployer=dingbaixia@mobike.com --service=gaea --tag_num=1.0.0 --typeid=1,2 --reportid=xxxx
 - 按测试用例运行 python main.py --env=brave --deployer=dingbaixia@mobike.com --service=gaea --tag_num=1.0.0 --caseid=1,2 --reportid=xxxx
 - 组合条件运行：同时指定优先级，测试用例，测试用例类型中的多个条件时，取各自测试用例，然后取交集
    ex: 运行优先级为1，2且有例的类型为3，4的所有测试用例： python main.py --env=brave --deployer=dingbaixia@mobike.com --service=gaea --tag_num=1.0.0 --priority=1,2 --typeid=3,4 --reportid=xxxx
 - 跑所有用例：不指定优先级，测试用例，测试用例类型任何条件时，跑所有的测试用例 python main.py --env=brave --deployer=dingbaixia@mobike.com --service=gaea --tag_num=1.0.0 --reportid=xxxx
 - 代码：
    ```
    def get_optionparser():
        parse = OptionParser()
        parse.add_option("-e", "--env", type="string", dest="env", help="被测的环境名")
        parse.add_option("-s", "--service", type="string", dest="service", help="被测的服务名")
        parse.add_option("-n", "--tag_num", type="string", dest="tag_num", help="被测服务的版本号")
        parse.add_option("-d", "--deployer", type="string", dest="deployer", help="打包人员邮件地址")
        parse.add_option("-t", "--typeid", type="string", dest="typeids", help="测试用例类型，从autotest.case_type中获取, ex: --type=1,2")
        parse.add_option("-p", "--priority", type="string", dest="prioritys", help="测试用例优先级, ex: --priority=1,2 ")
        parse.add_option("--caseid", type="string", dest="case_ids", help="测试用例ID集 , ex: --ids=1,2,3")
        parse.add_option("--reportid", type="string", dest="reportid", help="标识用例执行的唯一ID, 类型为整形")
        parse.add_option("--type", type="string", dest="run_type", help="-1表示跑门禁测试中添加组合条件，0表示门禁测试（is_ci=1，优先级为1，2），"
                                                                        "1表示ci全量测试(is_ci=1的所有用例), 2表示is_run为1的组合用例")
        parse.add_option("--emails", type="string", dest="receiver_list", help="收件人邮件列表")
        parse.add_option("--email_subject", type="string", dest="email_subject", help="email主题")
# 6. 工具使用
 - 基于swagger文档的python脚本生成工具
    - 描述：根据swagger文档，生成req,business, script相关的文件。重复执行不覆盖，目前只有新增。如果有接口变更，还需手动调整
    - 入口：tools/gencode/gen_sourcecode.py
    - 代码解读：
        ```
        if __name__ == "__main__":
            url_prefix = ""
            if len(sys.argv) < 2:
                #"POST /trialperiod/update/userTrialRecordPaidDepositInfo
                #生成某个接口
                url_list = [
                    "/dispatch/fencing/dispatchToAreas"
                    ]
                service = "gaea"
                # swagger文档url
                swagger_url = "http://10.201.62.129:8134/v2/api-docs"
                #生成swagger文档中所有的文档，请将注释去了
                #obj = ParseSwagger(swagger_url=swagger_url)
                #url_list = obj.all_paths.keys()
 - 数据库映射生成工具
    - 描述：生成数据库映射文件，生成的目录在lib/mbmanage/dbmanage/db_model下
    - 入口：tools/gencode/gen_dbmodel.py
    - 代码解读：
        ```
        if __name__ == "__main__":
            #需要作映射的数据库名，必填
            db_name = "mbk_modou"
            #需要作映射的表名，有表示只生成这个表的映射，为空字符串，表示生成数据下所有表的映射
            table_name = "mbk_modou_v2"
# 7. 详细文档
 - 框架文档 https://wiki.mobike.com/pages/viewpage.action?pageId=18662869