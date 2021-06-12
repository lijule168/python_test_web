"""
--------------------------------------
    date:   2018/3/20
--------------------------------------
    Change Date: 2018/3/20
    
"""
from lib.business.mysqldb.db_business import DBBusiness
from lib.entity.db_entity.db_table import DBTable
from lib.entity.db_entity.mbk_pay import MBKDepositInfo

__author__ = "dingbaixia@mobike.com"


class MBKDepositInfoBusiness(DBBusiness):
    def __init__(self):
        super(MBKDepositInfoBusiness, self).__init__(DBTable.MBKDepositInfo)

    def get_depositinfo_with_uid(self, user_id):
        """
        获取用户押金信息
        :param user_id:
        :return:
        """
        where = MBKDepositInfo()
        where.USER_ID = user_id
        items = self.query_with_column(where, MBKDepositInfo.select_column)

        if len(items) > 1:
            raise Exception("获取用户Balance信息出错")
        if len(items) == 0:
            return None

        item = items[0]
        obj = MBKDepositInfo()
        obj.DEPOSIT_ID = item[0]
        obj.USER_ID = item[1]
        obj.RMB = item[2]
        obj.TS = item[3]
        obj.CASH_SOURCE = item[4]
        obj.ISDELETE = item[5]
        obj.TIMELINESS = item[6]
        obj.CREATE_TIME = item[7]
        obj.UPDATE_TIME = item[8]
        obj.OPERATOR_ID = item[9]
        obj.STATUS = item[10]
        obj.ORDER_ID_FIRST = item[11]
        obj.ORDER_ID_SOURCE = item[12]
        obj.ORDER_ID_REFUND = item[13]
        obj.MOBILENO = item[14]
        obj.CURRENCY = item[15]
        obj.COUNTRY_CODE = item[16]
        obj.CITYCODE = item[17]
        obj.EXTEND1 = item[18]
        obj.EXTEND2 = item[19]
        obj.PAY_CHANNEL = item[20]

        return obj

    def add_depositinfo_record(self, user_id, rmb=0):
        """
        添加一条押金记录
        :param user_id:
        :param rmb:
        :return:
        """
        obj = MBKDepositInfo()
        obj.USER_ID = user_id
        obj.RMB = rmb
        DBBusiness(DBTable.MBKDepositInfo).add_record(obj)

