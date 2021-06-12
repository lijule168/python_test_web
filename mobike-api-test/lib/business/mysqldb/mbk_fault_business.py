# -*- coding:utf-8 -*-
from lib.util.log_util import l
from lib.entity.db_entity.db_table import DBTable
from lib.entity.db_entity.mbk_fault import MBKFaultCountryConf, MBKFaultTypeItem, MBKCustomerTicket
from lib.business.mysqldb.db_business import DBBusiness

class MBKFaultBusiness:

    def get_countryfaultitem(self, country_code=None, resolution=None, platform=None):
        faultconf_dict = self.get_faulttypeitem(resolution=resolution, platform=platform)
        countryconf_dict = self.get_faultcountryconf(country_code=country_code)
        countryfaultitem_dict = [(key, item) for key,item in countryconf_dict.items() if item.item_id in faultconf_dict.keys()]
        return countryfaultitem_dict

    def get_faulttypeitem(self, resolution=None, platform=None):
        '''
        获取fault配置信息
        :param resolution:
        :param platform:
        :return:
        '''
        where = MBKFaultTypeItem()
        if platform:
            where.platform = platform
        if resolution:
            where.resolution = resolution
        result = DBBusiness(DBTable.MBKFaultTypeItem).query_with_column(where, MBKFaultTypeItem.select_column)
        faultconf_dict = {}
        for item in result:
            faultconf = MBKFaultTypeItem()
            faultconf.id = item[0]
            faultconf.sub_type = item[1]
            faultconf.item_name = item[2]
            faultconf.icon_normal = item[3]
            faultconf.sort = item[4]
            faultconf.platform = item[5]
            faultconf.resolution = item[6]
            faultconf.icon_selected = item[7]
            faultconf.create_time = item[8]
            faultconf.update_time = item[9]
            faultconf_dict[faultconf.id] = faultconf
        return faultconf_dict

    def get_faultcountryconf(self, country_code=None, bike_type=None):
        '''
        获取城市故障配置
        :param country_code:
        :param bike_type:
        :return:
        '''
        where = MBKFaultCountryConf()
        if country_code:
            where.country_code = country_code
        if bike_type:
            where.bike_type = bike_type
        result = DBBusiness(DBTable.MBKFaultCountryConf).query_with_column(where, MBKFaultCountryConf.select_column)
        countryconf_dict = {}
        for item in result:
            countryconf = MBKFaultCountryConf()
            countryconf.id = item[0]
            countryconf.country_code = item[1]
            countryconf.bike_type = item[2]
            countryconf.item_id = item[3]
            countryconf.conf_status = item[4]
            countryconf.create_time = item[5]
            countryconf.update_time = item[6]
            countryconf_dict[countryconf.id] = countryconf
        return countryconf_dict

    def update_customerticket(self, ticket_id, create_time=None):
        '''
        更新ticket创建时间
        :param ticket_id:
        :param create_time:
        :return:
        '''
        where = MBKCustomerTicket()
        where.ticket_id = ticket_id
        update = MBKCustomerTicket()
        update.create_time = create_time
        DBBusiness(DBTable.MBKCustomerTicket).update_record(where, update)