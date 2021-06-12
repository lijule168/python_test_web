class GlobalEnv:
    pass

class DB:
    host = None
    port = None
    user_name = None
    passwd = None
    db_name = None

    def __str__(self):
        return "host:%s port:%s user_name:%s db_name:%s" % (self.host, self.port, self.user_name, self.db_name)


class MongoDB:
    host = None
    port = None
    user_name = None
    passwd = None

    def __str__(self):
        return "MongoDB connection string, host(%s), port(%s), user_name(%s), passwd(%s)" % (self.host,
                self.port, self.user_name, self.passwd)

class RedisService:
    host = None
    port = None
    passwd = None
    def __str__(self):
        return "redis host:%s, port:%s, passwd:%s" % (self.host, self.port, self.passwd)

class CodisService:
    host = None
    port = None
    passwd = None
    def __str__(self):
        return "codis host:%s, port:%s, passwd:%s" % (self.host, self.port, self.passwd)

class HttpService:
    mobike_api_host = None
    athena_host = None
    mercury_host = None
    mola_host = None

class MqttService:
    mqtt_host = None