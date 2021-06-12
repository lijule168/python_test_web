"""
--------------------------------------
    date:   2018/3/20
--------------------------------------
    Change Date: 2018/3/20
    
"""
from lib.business.mysqldb.db_business import DBBusiness
from lib.entity.db_entity.db_table import DBTable
from lib.entity.db_entity.mbk_db import MBKUsers

__author__ = "dingbaixia@mobike.com"

class MBKUsersBusiness(DBBusiness):
    def __init__(self):
        super(MBKUsersBusiness, self).__init__(DBTable.MBKUsers)

    def get_user_info_from_mbkuser(self, user_id):
        """
        根据userid获取用户信息
        :param user_id:
        :return:
        """
        where = MBKUsers()
        where.USERID = user_id
        items = self.query_with_column(where, MBKUsers.select_column)
        if len(items) > 1:
            raise Exception("获取用户membership信息出错")
        if len(items) == 0:
            return None
        item = items[0]

        obj_dict = self.convert_to_dict(MBKUsers.select_column, item)
        obj = MBKUsers()
        self.convert_dict_to_obj(obj_dict=obj_dict, dest_obj=obj)

        return obj

    def update_userinfo_by_userid(self, user_id, user_name=None, user_image=None, email=None, id_code=None, bz=None,
                                  img=None, nation=None, addr=None, sub_source=None):
        """
        更新User信息
        :param user_id:
        :param user_name:
        :return:
        """
        where = MBKUsers()
        where.USERID = user_id
        update = MBKUsers()
        if user_name:
            update.USERNAME = user_name
        if user_image:
            update.USERIMAGE = user_image
        if email:
            update.EMAIL = email
        if id_code:
            update.ID_CODE = id_code
        if bz:
            update.bz = bz
        if img:
            update.IMG = img
        if nation:
            update.NATION = nation
        if addr:
            update.ADDR = addr
        if sub_source:
            update.SUB_SOURCE = sub_source

        self.update_record(where_instance=where, update_instance=update)
