from lib.business.mysqldb.db_business import DBBusiness
from lib.entity.db_entity.db_table import DBTable
from lib.entity.db_entity.mbk_user_roaming import MBKUserRoaming


class MBKUserRoamingBusiness(object):
    def add_userroaming(self, user_id=None, mobile=None, region_city_code=None, region_country_code=None, region_dc_code=None,
                        roaming_city_code=None, roaming_country_code=None, roaming_dc_code=None, roaming_id=None,
                        roaming_result=None, roaming_state=None):
        obj = MBKUserRoaming()
        obj.user_id = user_id
        obj.mobile = mobile
        obj.region_city_code = region_city_code
        obj.region_country_code = region_country_code
        obj.region_dc_code = region_dc_code
        obj.roaming_city_code = roaming_city_code
        obj.roaming_country_code = roaming_country_code
        obj.roaming_dc_code = roaming_dc_code
        obj.roaming_id = roaming_id
        obj.roaming_result = roaming_result
        obj.roaming_state = roaming_state
        DBBusiness(DBTable.MBKUserRoaming).add_record(obj)


    def del_userroaming(self, user_id):
        where = MBKUserRoaming()
        where.user_id = user_id
        DBBusiness(DBTable.MBKUserRoaming).del_record(where_instance=where)

    def get_userroaming(self, roaming_id=None, user_id=None):
        where = MBKUserRoaming()
        if roaming_id:
            where.roaming_id = roaming_id
        if user_id:
            where.user_id = user_id
        records = DBBusiness(DBTable.MBKUserRoaming).query_with_column(where, MBKUserRoaming.select_column)
        # if len(records) != 1:
        #     raise Exception("查找数据库，数据库中的记录不为1")
        return records

