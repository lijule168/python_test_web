import redis

from lib.common.config_helper import EnvConfig
from lib.util.log_util import l

class RedisHelper(object):
    '''
    redis管理
    '''

    REDIS_CONN_POOL = {}

    def __init__(self):
        self.__init_conn()

    def __init_conn(self):
        redis_config = EnvConfig().mobike_redis_service
        key = redis_config.host.lower()
        if self.__class__.REDIS_CONN_POOL.get(key, ""):
            self.__redis_conn = self.__class__.REDIS_CONN_POOL[key]
            return
        try:
            l.info("init redis connection,(%s)"  % (redis_config.__str__()))
            pool = redis.ConnectionPool(host=redis_config.host, port=redis_config.port, db=0, password=redis_config.passwd)
            self.__redis_conn = redis.Redis(connection_pool=pool)
            self.__class__.REDIS_CONN_POOL[key] = self.__redis_conn
        except Exception as ex:
            l.error("inital redis connection failed, exception:%s" % (ex))
            raise ex

    def del_data(self, key):
        l.info("delete redis cache:key{%s}" % key)
        return self.__redis_conn.delete(key)

    def get_data(self, key):
        l.info("获取redis中的键值,key(%s)" % (key))
        return self.__redis_conn.get(key)

    def get_all_hash_subkey(self, primary_key):
        #l.info("获取hash key(%s)下所有的subkey" % primary_key)
        return self.__redis_conn.hgetall(primary_key)

    def set_data(self, key, value):
        l.info("在redis中设置键值,(key:%s, value:%s)" % (key, value))
        return self.__redis_conn.set(key, value)

    def is_exist(self, key):
        l.info("redis中是否存在key(%s)" % key)
        return self.__redis_conn.exists(key)

    def set_hash_data(self,key ,sub_key, sub_value):
        return self.__redis_conn.hset(key, sub_key, sub_value)

    def del_sub_key(self, key, sub_key):
        l.info("删除subkey, key(%s), subkey(%s)" % (key, sub_key))
        return self.__redis_conn.hdel(key, sub_key)
    def set_rpush(self, key, *value):
        # l.info("设置值, key(%s), value(%s)" % (key, value))
        return self.__redis_conn.rpush(key, *value)

    def get_key_expiretime(self, key):
        """
        获取key的过期时间
        :param key:
        :return:
        """
        return self.__redis_conn.ttl(key)

    def llen(self, key):
        """
        获取列表长度
        :param key:
        :return:
        """
        return self.__redis_conn.llen(key)

    def l_index(self, key, index):
        """
        获取某个索引的值
        :param key:
        :param index:
        :return:
        """
        return self.__redis_conn.lindex(key, index)

    def l_pop(self, key):
        """
        Remove and return the first item of the list ``name``
        :param key:
        :return:
        """
        return self.__redis_conn.lpop(key)

    def l_rpushx(self, key, value):
        """
        Push ``value`` onto the tail of the list ``name`` if ``name`` exists
        :param key:
        :param value:
        :return:
        """
        return self.__redis_conn.rpush(key, value)

    def publish(self, channel, msg):
        '''
        Publish ``message`` on ``channel``.
        Returns the number of subscribers the message was delivered to.
        :param channel:
        :param msg:
        :return:
        '''
        l.info("publish message(%s) on channel(%s)" % (msg, channel))
        try:
            return self.__redis_conn.publish(channel=channel, message=msg)
        except Exception as ex:
            l.error(ex)
            return None
