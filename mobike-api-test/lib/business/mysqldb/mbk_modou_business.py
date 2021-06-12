# -*- coding:utf-8 -*-
from lib.business.mysqldb.db_business import DBBusiness
from lib.util.log_util import l
from lib.business.orthrus.orthrus_basicinfo.price_business import PriceBusiness
from lib.business.user.user_business import UserBusiness
from lib.entity.db_entity.db_table import DBTable
from lib.entity.db_entity.mbk_modou1 import MBKModouV2

class MBKModouBusiness:
    def get_user_modou(self, user_id):
        '''
        获取用户魔豆信息
        :param user_id:
        :return:
        '''
        where = MBKModouV2()
        where.user_id = user_id
        results = DBBusiness(DBTable.MBKModouV2).query_with_column(where, MBKModouV2.select_column)
        #"modou_id, user_id, city_code, type, exchange_status, order_id, activity_id, modou, description, " \
        #"has_apply, is_delete, crt_time, upd_time, apply_expire_time, expire_time"
        usermodou_list = []
        for item in results:
            obj = MBKModouV2()
            obj.modou_id = item[0]
            obj.user_id = item[1]
            obj.city_code = item[2]
            obj.type = item[3]
            obj.exchange_status = item[4]
            obj.order_id = item[5]
            obj.activity_id = item[6]
            obj.modou = item[7]
            obj.description = item[8]
            obj.has_apply = item[9]
            obj.is_delete = item[10]
            obj.crt_time = item[11]
            obj.upd_time = item[12]
            obj.apply_expire_time = item[13]
            obj.expire_time = item[14]
            usermodou_list.append(obj)

        return usermodou_list