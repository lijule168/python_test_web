from lib.common.config_helper import EnvConfig
from lib.common.mysql_helper import MysqlHelper
from lib.entity.mustang_struct import DataCenterCode
from lib.util.log_util import l


class EnvBusiness(object):

    @classmethod
    def set_env(cls, datacenter):
        """
        设置测试环境（切换环境）
        :param datacenter:
        :return:
        """
        l.info("设置当前环境为：{0}".format(datacenter))
        EnvConfig().set_env(index=datacenter.value)

    @classmethod
    def get_current_env(cls):
        """
        获取当前的环境信息
        :return:
        """
        return EnvConfig().current_env

    @classmethod
    def get_all_env(cls):
        """
        :return:
        """
        return EnvConfig().configs

    @classmethod
    def clean_env(cls):
        """
        清除连接
        :return:
        """
        for key in MysqlHelper.DB_CONN_POOL.keys():
            if not MysqlHelper.DB_CONN_POOL[key]._closed:
                MysqlHelper.DB_CONN_POOL[key].close()

    @classmethod
    def switch_env(cls):
        '''
        切换环境
        :return:
        '''

        if 2 == EnvBusiness.get_current_env().dc_code:
            EnvBusiness.set_env(DataCenterCode.ZH)
        elif 0 == EnvBusiness.get_current_env().dc_code:
            EnvBusiness.set_env(DataCenterCode.EU)

