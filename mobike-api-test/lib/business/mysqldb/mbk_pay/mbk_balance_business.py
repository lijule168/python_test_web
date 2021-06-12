"""
--------------------------------------
    date:   2018/3/20
--------------------------------------
    Change Date: 2018/3/20
    
"""
import json

import datetime

from lib.business.mysqldb.db_business import DBBusiness
from lib.entity.db_entity.db_table import DBTable
from lib.entity.db_entity.mbk_pay import MBKBalance

__author__ = "dingbaixia@mobike.com"


class MBKBalanceBusiness(DBBusiness):
    def __init__(self):
        super(MBKBalanceBusiness, self).__init__(DBTable.MBKBalance)

    def get_balanceinfo_with_uid(self, user_id):
        """
        获取用户余额信息
        :param user_id:
        :return:
        """
        where = MBKBalance()
        where.USERID = user_id
        items = self.query_with_column(where, MBKBalance.select_column)
        if len(items) > 1:
            raise Exception("获取用户Balance信息出错")
        if len(items) == 0:
            return None

        item = items[0]

        obj_dict = self.convert_to_dict(MBKBalance.select_column, item)
        obj = MBKBalance()
        self.convert_dict_to_obj(obj_dict=obj_dict, dest_obj=obj)

        return obj

    def add_balance_record(self, user_id):
        """
        给用户添加余额
        :param user_id:
        :return:
        """
        obj = MBKBalance()
        obj.USERID = user_id
        DBBusiness(DBTable.MBKBalance).add_record(obj)


if __name__ == "__main__":
    MBKBalanceBusiness().get_balanceinfo_with_uid(user_id=3634335107748056534016159489)