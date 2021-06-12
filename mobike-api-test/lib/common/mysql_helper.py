import pymysql
from pymysql.constants import SERVER_STATUS
from lib.entity.run_config import RunCaseConfig
from lib.util.log_util import l


class MysqlHelper:
    DB_CONN_POOL = {}

    def __init__(self, conn_obj):
        if str(conn_obj.host).startswith("mysql"):
            env = conn_obj.host.split(".")[1]
            if env != RunCaseConfig.instance().env:
                conn_obj.host = conn_obj.host.replace(env, RunCaseConfig.instance().env)
        if MysqlHelper.DB_CONN_POOL.get(conn_obj.host, ""):
            self.__db_conn = MysqlHelper.DB_CONN_POOL[conn_obj.host]
            #l.debug("sql 状态{0}".format(self.__db_conn.server_status))
            if self.__db_conn._closed:
                l.debug("连接断开，重连, {0}".format(self.__db_conn))
                self.__db_conn = self.__init_conn(conn_obj)
                MysqlHelper.DB_CONN_POOL[conn_obj.host] = self.__db_conn

            try:
                self.__db_conn.select_db(conn_obj.db_name)
            except Exception as ex:
                l.error("选择DB失败， ex:{0}".format(ex))
                try:
                    self.__db_conn.close()
                except Exception as ex:
                    l.error("关闭连接失败， ex:{0}".format(ex))
                self.__db_conn = self.__init_conn(conn_obj)
                MysqlHelper.DB_CONN_POOL[conn_obj.host] = self.__db_conn
        else:
            self.__db_conn = self.__init_conn(conn_obj)
            MysqlHelper.DB_CONN_POOL[conn_obj.host] = self.__db_conn

        try:
            self.__db_conn.ping()
        except Exception as ex:
            l.warn("mysql链接失效, Exception:{0}".format(ex))
            # if self.__db_conn:
            #     self.__db_conn.close()
            self.__db_conn = self.__init_conn(conn_obj)
            MysqlHelper.DB_CONN_POOL[conn_obj.host] = self.__db_conn

    def __init_conn(self, conn_obj):
        '''
        获取数据库连接
        :param server:数据库服务的ip地址或domain
        :param port:
        :param user:
        :param passwd:
        :param db_name:
        :return:
        '''
        try:
            l.info("connect to db: %s" % conn_obj.__str__())
            __db_conn = pymysql.connect(host=conn_obj.host, port=int(conn_obj.port), db=conn_obj.db_name, user=conn_obj.user_name, passwd=conn_obj.passwd, charset="utf8")
            __db_conn.autocommit(True)
            return __db_conn
        except Exception as ex:
            l.error("connect to db failed, Exception:{0}".format(ex))
            raise Exception("connect to db failed, connstr:{0} Exception:{1}".format(conn_obj, ex))

    def execute_query_records(self, sql_statement, args=None):
        '''
        执行查询操作
        :param cmd: sql statement
        :param args: sql params
        :return:
        '''
        msg = "execute statement: {0}, args:{1} ".format(sql_statement, args)
        l.info(msg)
        try:
            with self.__db_conn.cursor() as cursor:
                cursor.execute(sql_statement, args)
                records = cursor.fetchall()
                self.__db_conn.commit()
                return records
        except Exception as e:
            l.error("{0} failed, Exception: {1}".format(msg, e))
            raise e
        # finally:
        #     if self.__db_conn:
        #         self.__db_conn.close()

    def execute_non_query_cmd(self, sql_statement, args=None):
        msg = "execute statement: {0}, args:{1} ".format(sql_statement, args)
        l.info(msg)
        try:
            with self.__db_conn.cursor() as cursor:
                cursor.execute(sql_statement, args)
                self.__db_conn.commit()
        except Exception as e:
            l.error("{0} failed, Exception: {1}".format(msg, e))
            self.__db_conn.rollback()
            raise e
        # finally:
        #     if self.__db_conn:
        #         self.__db_conn.close()

# if __name__ == "__main__":
#     pass