# -*- coding:utf-8 -*-
from lib.util.log_util import l
from lib.business.orthrus.orthrus_basicinfo.price_business import PriceBusiness
from lib.business.user.user_business import UserBusiness
from lib.entity.db_entity.db_table import DBTable
from lib.entity.db_entity.mbk_orthrus import MBKPrice, MBKHeaderPicture, MBKStation, MBKPlatformApplication, MBKOrder, MBKOrderDetail, MBKOrderStatus, MBKUserRelation, MBKActivityThirdparty
from lib.business.mysqldb.db_business import DBBusiness
from lib.util.random_util import RandomUtil


class MBKOrthusBusiness:
    wuhan_subway_application_id = "316257894993566720"
    def regist_3rdparty(self, application_id=None, phone=None):
        '''
        创建关联账号信息
        :param application_id:
        :return:
        '''
        if not application_id:
            application_id = self.__class__.wuhan_subway_application_id
        response = UserBusiness().register_new_user(mobile_num=phone)
        try:
            PriceBusiness().getprice(header_applicationid=application_id, header_accesstoken=response['authtoken'],
                                                header_userid=response["userid"],
                                                startStationId=1, endStationId=2, header_citycode="027"
                                                )
            obj = self.get_userrelation(application_id=application_id, mobike_uid=response['userid'])[0]
        except Exception as ex:
            l.error("创建关联账号信息失败，{0}".format(ex))
            raise ex
        return obj

    def add_application(self, city_code=None, country_code=None, application_type=None, application_name=None):
        obj = MBKPlatformApplication()
        obj.country_code = "CN"
        obj.city_code = "0792"
        obj.application_type = 0
        obj.application_name = "0792_测试地铁取票码"
        obj.status = 1
        DBBusiness(DBTable.MBKPlatformApplication).add_record(obj)

    def del_order_info(self, application_id=None, order_no=None):
        '''
        删除order数据库信息
        :param application_id:
        :param order_no:
        :return:
        '''
        obj = MBKOrder()
        if application_id:
            obj.application_id = application_id
        if order_no:
            obj.order_no = order_no
        DBBusiness(DBTable.MBKOrder).del_record(obj)

    def add_order_info(self, application_id=None, order_id=None, order_no=None, status=None, ticket_code=None, amount=None, real_amount=None,
                       relation_id=1):
        '''添加一条订单记录'''
        obj = MBKOrder()
        obj.status = status
        obj.application_id = application_id
        obj.order_no = order_no
        obj.ticket_code = ticket_code
        obj.amount = amount
        obj.real_amount = real_amount
        obj.order_id = order_id
        obj.price_snapshot_id = 1
        obj.relation_id = 1
        DBBusiness(DBTable.MBKOrder).add_record(obj)

    def get_order_info(self, application_id, order_no):
        '''
        获取订单信息
        :param application_id:
        :param order_no:
        :return:
        '''
        obj = MBKOrder()
        obj.order_no = order_no
        obj.application_id = application_id
        record =DBBusiness(DBTable.MBKOrder).query_with_column(obj, "order_id,order_no,relation_id,application_id,status,"
                                                            "price_snapshot_id,ticket_total,amount,real_amount,ticket_code,"
                                                            "pay_channel,order_type,create_time,update_time")[0]
        order_info = MBKOrder()
        order_info.order_id = record[0]
        order_info.order_no = record[1]
        order_info.relation_id = record[2]
        order_info.application_id = record[3]
        order_info.status = record[4]
        order_info.price_snapshot_id = record[5]
        order_info.ticket_total = record[6]
        order_info.amount = record[7]
        order_info.real_amount = record[8]
        order_info.ticket_code = record[9]
        order_info.pay_channel = record[10]
        order_info.order_type = record[11]
        order_info.create_time = record[12]
        order_info.update_time = record[13]
        return order_info

    def get_mbkprice_with_mbkpriceobj(self, application_id=None, start_station_id=None, end_station_id=None):
        obj = MBKPrice()
        obj.application_id = application_id
        obj.start_station_id = start_station_id
        obj.end_station_id = end_station_id
        # record = DBBusiness(DBTable.OrcPrice).query(obj, "price", "start_station_id", "end_station_id", "application_id")[0]
        record = \
        DBBusiness(DBTable.MBKPrice).query_with_column(obj, "price,start_station_id,end_station_id,application_id")[0]
        price_detail = MBKPrice()
        price_detail.price = record[0]
        price_detail.start_station_id = record[1]
        price_detail.end_station_id = record[2]
        price_detail.application_id = record[3]
        return price_detail

    def get_station_detail_withsationobj(self, station_id):
        '''
        获取station信息
        :param station_id:
        :return:
        '''
        station = MBKStation()
        station.station_id = station_id
        record = DBBusiness(DBTable.MBKStation).query(station, "station_id","station_code", "station_name", "station_name_en")[0]
        obj = MBKStation()
        obj.station_id = record[0]
        obj.station_code = record[1]
        obj.station_name = record[2]
        obj.station_name_en = record[3]

        return obj

    def get_line_detail(self, application_id=None, line_id=None, is_started=None, station_name=None, station_name_en=None):
        '''
        获取line信息
        :param application_id:
        :param line_id:
        :param is_started:
        :param station_name:
        :param station_name_en:
        :return:
        '''
        station = MBKStation()
        station.application_id = application_id
        station.line_id = line_id
        station.station_name = station_name
        record = DBBusiness(DBTable.MBKStation).query_with_column(station, "station_first_letter, last_station_id, station_name_en, "
                                                                           "next_station_id, station_id")

    def del_price(self, price_entity):
        '''
        删除价格表记录
        :param price_entity:
        :return:
        '''
        price = MBKPrice()
        price.start_station_id = price_entity.startStationId
        price.end_station_id = price_entity.endStationId
        price.application_id = price_entity.applicationId
        DBBusiness(DBTable.MBKPrice).del_record(price)

    def get_userrelation(self, application_id, mobike_uid):
        '''
        获取用户与三方的关系表
        :param application_id:
        :param mobike_uid:
        :return:
        '''
        user_relation = MBKUserRelation()
        user_relation.application_id = application_id
        user_relation.mobike_uid = mobike_uid
        record = DBBusiness(DBTable.MBKUserRelation).query_with_column(user_relation, MBKUserRelation.select_column)
        user_relation_list = []
        for item in record:
            obj = MBKUserRelation()
            obj.relation_id = item[0]
            obj.mobike_uid = str(item[1])
            obj.thirdparty_uid = str(item[2])
            obj.application_id = str(item[3])
            user_relation_list.append(obj)

        return user_relation_list

    def del_order_detail_info(self, application_id=None, order_id=None, mobike_uid=None, order_no=None):
        '''
        删除详细订单信息
        :param application_id:
        :param order_id:
        :param mobike_uid:
        :param order_no:
        :return:
        '''
        detail = MBKOrderDetail()
        if application_id:
            detail.application_id = application_id
        if order_id:
            detail.order_id = order_id
        if mobike_uid:
            detail.mobike_uid = mobike_uid
        if order_no:
            detail.order_no = order_no
        DBBusiness(DBTable.MBKOrderDetail).del_record(detail)

    def add_order_detail_info(self, order_detail_id=None, order_id=None, order_no=None, relation_id=1, mobike_uid=None,
                              thirdparty_uid=None, application_id=None, start_line_id=1, start_line_name=None,
                              start_station_id=2, start_station_name=None, end_line_id="2", end_line_name=None,
                              end_station_id="25", end_station_name=None, price_snapshot_id=1, price=None, status=0,
                              ticket_total=0, ticket_real=0, amount=None, real_amount=None, ticket_code=None,
                              activity_id=None, pay_channel=0, order_type=0, orc_order_no=None):
        '''
        添加订单详细信息
        :param order_detail_id:
        :param order_id:
        :param order_no:
        :param relation_id:
        :param mobike_uid:
        :param thirdparty_uid:
        :param application_id:
        :param start_line_id:
        :param start_line_name:
        :param start_station_id:
        :param start_station_name:
        :param end_line_id:
        :param end_line_name:
        :param end_station_id:
        :param end_station_name:
        :param price_snapshot_id:
        :param price:
        :param status:
        :param ticket_total:
        :param ticket_real:
        :param amount:
        :param real_amount:
        :param ticket_code:
        :param activity_id:
        :param pay_channel:
        :param order_type:
        :param orc_order_no:
        :return:
        '''
        detail = MBKOrderDetail()
        if order_detail_id:
            detail.order_detail_id = order_detail_id

        detail.order_id = order_id
        detail.order_no = order_no
        detail.relation_id = relation_id
        detail.mobike_uid = mobike_uid
        detail.thirdparty_uid = thirdparty_uid
        detail.application_id = application_id
        detail.start_line_id = start_line_id
        detail.start_line_name = start_line_name
        detail.start_station_id = start_station_id
        detail.start_station_name = start_station_name
        detail.end_line_id = end_line_id
        detail.end_line_name = end_line_name
        detail.end_station_id = end_station_id
        detail.end_station_name = end_station_name
        detail.price_snapshot_id = price_snapshot_id
        detail.price = price
        detail.status = status
        detail.ticket_total = ticket_total
        detail.ticket_real = ticket_real
        detail.amount = amount
        detail.real_amount = real_amount
        detail.ticket_code = ticket_code
        detail.activity_id = activity_id
        detail.pay_channel = pay_channel
        detail.order_type = order_type
        if orc_order_no:
            detail.orc_order_no = orc_order_no
        else:
            detail.orc_order_no = RandomUtil.get_order_id()
        # detail.create_time = item[26]
        # detail.update_time = item[27]
        DBBusiness(DBTable.MBKOrderDetail).add_record(detail)


    def get_order_detail_info(self, relation_id, mobike_uid, thirtparty_id, application_id):
        '''
        获取MBKUserDetail信息
        :param relation_id:
        :param mobike_uid:
        :param thirtparty_id:
        :param application_id:
        :return:
        '''
        user_relation = MBKUserRelation()
        user_relation.application_id = application_id
        user_relation.mobike_uid = mobike_uid
        user_relation.relation_id = relation_id
        user_relation.thirdparty_uid = thirtparty_id
        record = DBBusiness(DBTable.MBKOrderDetail).query_with_column(user_relation, MBKOrderDetail.select_columns)
        detail_list = []
        #"order_detail_id ,order_id ,order_no ,relation_id ,mobike_uid ,thirdparty_uid ,application_id ,start_line_id ,
        # start_line_name ,start_station_id ,start_station_name ,end_line_id ,end_line_name ,end_station_id ,
        # end_station_name ,price_snapshot_id ,price ,status ,ticket_total ,ticket_real ,amount ,real_amount ,ticket_code ,
        # activity_id ,pay_channel ,order_type ,create_time ,update_time"
        for item in record:
            detail = MBKOrderDetail()
            detail.order_detail_id = item[0]
            detail.order_id = item[1]
            detail.order_no = item[2]
            detail.relation_id = item[3]
            detail.mobike_uid = item[4]
            detail.thirdparty_uid = item[5]
            detail.application_id = item[6]
            detail.start_line_id = item[7]
            detail.start_line_name = item[8]
            detail.start_station_id = item[9]
            detail.start_station_name = item[10]
            detail.end_line_id = item[11]
            detail.end_line_name = item[12]
            detail.end_station_id = item[13]
            detail.end_station_name = item[14]
            detail.price_snapshot_id = item[15]
            detail.price = item[16]
            detail.status = item[17]
            detail.ticket_total = item[18]
            detail.ticket_real = item[19]
            detail.amount = item[20]
            detail.real_amount = item[21]
            detail.ticket_code = item[22]
            detail.activity_id = item[23]
            detail.pay_channel = item[24]
            detail.order_type = item[25]
            detail.create_time = item[26]
            detail.update_time = item[27]
            detail_list.append(detail)

        return detail_list

    def add_station(self, application_id=None, station_id=None, station_code=None, station_name=None, station_name_en=None,
                    city_code="010", line_id="1", is_transfer_station=0, last_station_id=1, next_station_id=None,
                    machine_position="A口附近"):
        '''
        添加站点信息
        :param application_id:
        :param station_id:
        :param station_code:
        :param station_name:
        :param station_name_en:
        :param city_code:
        :param line_id:
        :param is_transfer_station:
        :param last_station_id:
        :param next_station_id:
        :param machine_position:
        :return:
        '''
        obj = MBKStation()
        obj.application_id = application_id
        obj.status = 1
        obj.station_id = station_id
        obj.station_code = station_code
        obj.station_name = station_name
        obj.station_name_en = station_name_en
        obj.city_code = city_code
        obj.line_id = line_id
        obj.is_transfer_station = is_transfer_station
        obj.last_station_id = last_station_id
        obj.next_station_id = next_station_id
        if next_station_id is None:
            obj.next_station_id = int(station_id) + 1
        obj.station_first_letter = ""
        if obj.station_name_en:
            obj.station_first_letter = obj.station_name_en[0]
        obj.machine_position = machine_position
        obj.visible = 0
        obj.server_version = "1.0"
        DBBusiness(DBTable.MBKStation).add_record(obj)

    def del_station(self, appliation_id, station_id, station_name=None):
        '''
        删除站点信息
        :param appliation_id:
        :param station_id:
        :param station_name:
        :return:
        '''
        obj = MBKStation()
        obj.application_id = appliation_id
        obj.station_id = station_id
        obj.station_name = station_name
        DBBusiness(DBTable.MBKStation).del_record(obj)

    def get_stations(self, application_id=None, station_name=None, is_start=None):
        '''
        获取站点信息
        :param application_id:
        :param station_name:
        :param is_start:
        :return:
        '''
        obj = MBKStation()
        if application_id:
            obj.application_id = application_id
        if station_name:
            obj.station_name = station_name
        # if is_start:
        #     obj.st
        DBBusiness(DBTable.MBKStation).query_with_column(obj, MBKStation.select_column)


    def add_activity_thirdparty(self, application_id=None, activity_content=None, activity_id=None,  order_id=None):
        '''
        添加活动信息
        :param application_id:
        :param activity_content:
        :param activity_id:
        :param order_id:
        :return:
        '''
        obj = MBKActivityThirdparty()
        obj.application_id = application_id
        obj.activity_content = activity_content
        obj.activity_thirdparty_id = activity_id
        if order_id:
            obj.order_id = order_id
        obj.order_id = RandomUtil.get_long()
        DBBusiness(DBTable.MBKActivityThirdparty).add_record(obj)

    def del_activity_thirdparty(self, activity_id=None, order_id=None):
        '''
        删除活动信息
        :param activity_id:
        :param order_id:
        :return:
        '''
        obj = MBKActivityThirdparty()
        if activity_id:
            obj.activity_thirdparty_id = activity_id
        if order_id:
            obj.order_id = order_id
        DBBusiness(DBTable.MBKActivityThirdparty).del_record(obj)

    def del_header_picture(self, application_id, citycode):
        '''
        删除header banner
        :param application_id:
        :param citycode:
        :return:
        '''
        obj = MBKHeaderPicture()
        if application_id:
            obj.application_id = application_id
        if citycode:
            obj.city_code = citycode
        DBBusiness(DBTable.MBKHeaderPicture).del_record(obj)

    def get_header_picture(self, application_id, citycode):
        '''
        获取header banner
        :param application_id:
        :param citycode:
        :return:
        '''
        obj = MBKHeaderPicture()
        if application_id:
            obj.application_id = application_id
        if citycode:
            obj.city_code = citycode
        r_db = DBBusiness(DBTable.MBKHeaderPicture).query_with_column(obj, MBKHeaderPicture.select_columns)[0]
        r_obj = MBKHeaderPicture()
        r_obj.header_picture_id = r_db[0]
        r_obj.enabled = r_db[3]
        return r_obj

