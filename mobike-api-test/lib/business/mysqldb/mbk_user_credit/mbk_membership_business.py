"""
--------------------------------------
    date:   2018/3/20
--------------------------------------
    Change Date: 2018/3/20
    
"""
from lib.business.mysqldb.db_business import DBBusiness
from lib.entity.db_entity.db_table import DBTable
from lib.entity.db_entity.mbk_user_credit import MBKMembership
from lib.util.time_util import TimeUtil

__author__ = "dingbaixia@mobike.com"


class MBKMemberShipBusiness(DBBusiness):
    def __init__(self):
        super(MBKMemberShipBusiness, self).__init__(DBTable.MBKMembership)

    def get_membership_byuid(self, user_id):
        where = MBKMembership()
        where.user_id = user_id
        items = self.query_with_column(where, MBKMembership.select_column)
        if len(items) > 1:
            raise Exception("获取用户membership信息出错")
        if len(items) == 0:
            return None
        item = items[0]
        obj = MBKMembership()
        obj.user_id = item[0]
        obj.user_name = item[1]
        obj.city_code = item[2]
        obj.country_code = item[3]
        obj.mobile_no = item[4]
        obj.level = item[5]
        obj.crt_time = item[6]
        obj.free_time = item[7]
        obj.member_time = item[8]
        obj.quit_time = item[9]
        obj.super_time = item[10]
        obj.upd_time = item[11]
        obj.is_delete = item[12]

        return obj

    def add_membership_record(self, user_id, user_name=None, city_code="010", country_code="0", level=1, free_time=None,
                              member_time=None, quit_time=None, super_time=None):
        """
        插入一条membership记录
        :param user_id:
        :return:
        """
        obj = MBKMembership()
        obj.user_id = user_id
        if user_name:
            obj.user_name = user_name
        if city_code:
            obj.city_code = city_code
        if country_code:
            obj.country_code = country_code
        if level:
            obj.level = level
        if not free_time:
            obj.free_time = TimeUtil.format_timer_to_str()
        else:
            obj.free_time = free_time
        if not member_time:
            obj.member_time = TimeUtil.format_timer_to_str()
        else:
            obj.member_time = member_time
        if not quit_time:
            obj.quit_time = TimeUtil.format_timer_to_str()
        else:
            obj.quit_time = quit_time
        if not super_time:
            obj.super_time = TimeUtil.format_timer_to_str()
        else:
            obj.super_time = super_time

        DBBusiness(DBTable.MBKMembership).add_record(obj)