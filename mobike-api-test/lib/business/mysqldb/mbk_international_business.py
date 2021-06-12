from lib.entity.db_entity.db_table import DBTable
from lib.entity.db_entity.mbk_international import MBKDomainConfig
from lib.business.mysqldb.db_business import DBBusiness

class MBKInternationalBusiness:
    def add_domainconfig(self, name, type, domain, mapped_domain):
        """
        添加domain配置
        :param name:
        :param type:
        :param domain:
        :param mapped_domain:
        :return:
        """
        obj = MBKDomainConfig()
        obj.name = name
        obj.type = type
        obj.domain = domain
        obj.mapped_domain = mapped_domain
        DBBusiness(DBTable.MBKDomainConfig).add_record(obj)

    def del_domainconfig(self, name, type, domain):
        """
        删除domain配置
        :param name:
        :param type:
        :param domain:
        :return:
        """
        where = MBKDomainConfig()
        where.name = name
        where.type = type
        where.domain = domain
        DBBusiness(DBTable.MBKDomainConfig).del_record(where_instance=where)