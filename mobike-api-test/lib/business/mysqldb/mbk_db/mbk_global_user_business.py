"""
--------------------------------------
    date:   2018/3/20
--------------------------------------
    Change Date: 2018/3/20
    
"""
from lib.business.mysqldb.db_business import DBBusiness
from lib.entity.db_entity.db_table import DBTable
from lib.entity.db_entity.mbk_db import MBKGlobalUser

__author__ = "dingbaixia@mobike.com"


class MBKGlobalUserBusiness(DBBusiness):
    def __init__(self):
        super(MBKGlobalUserBusiness, self).__init__(DBTable.MBKGlobalUser)

    def get_global_userinfo_from_mbkglobaluser(self, user_id):
        """
        根据userid获取globaluserinfo
        :param user_id:
        :return:
        """
        where = MBKGlobalUser()
        where.userId = user_id
        items = self.query_with_column(where, MBKGlobalUser.select_column)

        if len(items) > 1:
            raise Exception("获取用户membership信息出错")
        if len(items) == 0:
            return None
        item = items[0]
        obj = MBKGlobalUser()
        obj.userId = item[0]
        obj.agreeMarketing = item[1]
        obj.meetLegalAge = item[2]
        obj.stripeCountry = item[3]
        obj.agree_to_sms = item[4]
        obj.agree_to_push = item[5]
        obj.agree_to_email = item[6]
        obj.create_time = item[7]
        obj.update_time = item[8]
        obj.agree_to_required_consent = item[9]

        return obj

    def add_globaluserinfo_record(self, user_id):
        """
        添加一条记录
        :param user_id:
        :return:
        """
        obj = MBKGlobalUser()
        obj.userId = user_id
        self.add_record(obj)


