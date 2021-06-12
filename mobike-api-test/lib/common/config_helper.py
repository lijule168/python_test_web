import os, yaml, configparser

from lib.entity.env_config import *
from lib.entity.run_config import *
from lib.util.path_util import config_path

class RunConfig(object):
    __instance = None
    runcase_user_config = RunCaseUserConfig()
    autotest_db_conn_str = DB()
    email_config = EmailConfig()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(RunConfig, cls).__new__(cls, *args, **kwargs)
            cls.__instance.parser_config()
        return cls.__instance

    def parser_config(self):
        config = configparser.ConfigParser()
        try:
            config.read(config_path + "run_conf.ini")
            runcase_config = RunCaseConfig.instance()
            runcase_config.case_ids = eval(config["RUNCASECONFIG"]["case_id"])
            runcase_config.case_type_ids = eval(config["RUNCASECONFIG"]["case_type_id"])
            runcase_config.env = config["RUNCASECONFIG"]["env"]
            runcase_config.runmode = int(config["RUNCASECONFIG"]["runmode"])
            runcase_config.receiver_list = eval(config["RUNCASECONFIG"]["receviers"])

            self.runcase_user_config.run_one_user = config["RUNCASEUSERCONFIG"]["run_one_user"]
            if runcase_config.env == "toronto":
                self.runcase_user_config.run_user_mobileNo = config["RUNCASEUSERCONFIG"]["run_user_torontoNo"]
            else:
                self.runcase_user_config.run_user_mobileNo = config["RUNCASEUSERCONFIG"]["run_user_mobileNo"]

            self.autotest_db_conn_str.host = config["autotest_db"]["host"]
            self.autotest_db_conn_str.port = config["autotest_db"]["port"]
            self.autotest_db_conn_str.user_name = config["autotest_db"]["user"]
            self.autotest_db_conn_str.passwd = config["autotest_db"]["passwd"]
            self.autotest_db_conn_str.db_name = config["autotest_db"]["db"]
        except Exception as ex:
            raise ex

class EnvConfig(object):
    __instance = None
    __configs = None
    current_env = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(EnvConfig, cls).__new__(cls, *args, **kwargs)
            configs = YamlHelper().all_config
            cls.__instance.configs = configs
            cls.__instance.current_env = configs[YamlHelper().current_env]
        return cls.__instance

    def set_env(self, index=0):
        """
        设置环境信息
        :param index: default值是0，不传入表示还原
        :return:
        """
        if self.configs.keys().__len__() > 1 or self.configs.keys().__len__() > index:
            key = list(self.configs.keys())[index]
            RunCaseConfig.instance().env = self.configs[key].env
            self.current_env = self.configs[key]
        else:
            key = list(self.configs.keys())[YamlHelper().current_env]
            RunCaseConfig.instance().env = self.configs[key].env
            self.current_env = self.configs[key]
        return self.configs[key]

    @property
    def mobkie_db_conn_params(self):
        return self.current_env.mobkie_db_conn_params

    @property
    def mobike_http_service(self):
        return self.current_env.mobike_http_service

    @property
    def mobike_mqtt_service(self):
        return self.current_env.mobike_mqtt_service

    @property
    def mobike_mongdb_service(self):
        return self.current_env.mobike_mongdb_service

    @property
    def mobike_redis_service(self):
        return self.current_env.mobike_redis_service

    @property
    def mobike_codis_service(self):
        return self.current_env.mobike_codis_service

class Config(object):
    mobike_http_service = None
    mobike_codis_service = None
    mobkie_db_conn_params = None
    mobike_mongdb_service = None
    mobike_mqtt_service = None
    mobike_redis_service = None
    env = None
    dc_code = None

class YamlHelper(object):
    all_config = {}
    __instance = None
    __env = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(YamlHelper, cls).__new__(cls, *args, **kwargs)
            cls.__instance.__env = RunCaseConfig().instance().env
            cls.all_config = cls.__instance.parse_yaml()

        return cls.__instance

    def parse_yaml(self):
        file_path = config_path + os.sep + "env_" + self.__env + ".yaml"
        if not os.path.exists(file_path):
            file_path = config_path + os.sep + "env_template.yaml"
        with open(file_path, encoding="utf-8") as f:
            content = f.read().replace('{env}', self.__env)
            config = yaml.load_all(content)
            all_env_config = {}
            for env_config in config:
                for env in env_config:
                    obj = Config()
                    obj.mobike_http_service = self.__get_http_service(env_config[env])
                    obj.mobike_codis_service = self.__get_codis_service_info(env_config[env])
                    obj.mobkie_db_conn_params = self.__get_db_connstr_with_nodb(env_config[env], "mobike_db")
                    obj.mobike_mongdb_service = self.__get_mongodb_connstr(env_config[env])
                    obj.mobike_mqtt_service = self.__get_mqtt_service(env_config[env])
                    obj.mobike_redis_service = self.__get_redis_service_info(env_config[env])
                    obj.env = env
                    obj.dc_code = int(env_config[env]["DC_CODE"])
                    all_env_config[obj.dc_code] = obj
                    if env == RunCaseConfig().instance().env:
                        self.current_env = int(env_config[env]["DC_CODE"])
            return all_env_config

    def __get_http_service(self, env_config):
        http_service = HttpService()
        http_service.mobike_api_host = env_config["mobike_service"]["mobike_api_host"].replace('{env}', self.__env)
        http_service.athena_host = env_config["mobike_service"]["athena_host"].replace('{env}', self.__env)
        http_service.mercury_host = env_config["mobike_service"]["mercury_host"].replace('{env}', self.__env)
        http_service.mola_host = env_config["mobike_service"]["mola_host"].replace('{env}', self.__env)

        return http_service

    def __get_mqtt_service(self, env_config):
        __mqtt_service = MqttService()
        __mqtt_service.mqtt_host = env_config["mqtt"]["host"].replace('{env}', self.__env)
        return __mqtt_service

    def __get_db_connstr_with_nodb(self, env_config, db_config_key):
        db_conn_str = DB()
        db_conn_str.host = env_config[db_config_key]["host"].replace('{env}', self.__env)
        db_conn_str.port = env_config[db_config_key]["port"]
        db_conn_str.user_name = env_config[db_config_key]["user"]
        db_conn_str.passwd = env_config[db_config_key]["passwd"]
        db_conn_str.db_name = env_config[db_config_key]["db"]
        return db_conn_str

    def __get_mongodb_connstr(self, env_config):
        mongodb_conn_str = MongoDB()
        mongodb_conn_str.host = env_config["mongo_db"]["host"].replace('{env}', self.__env)
        mongodb_conn_str.port = env_config["mongo_db"]["port"]
        mongodb_conn_str.user_name = env_config["mongo_db"]["user"]
        mongodb_conn_str.passwd = env_config["mongo_db"]["passwd"]
        return mongodb_conn_str

    def __get_redis_service_info(self, env_config):
        redis_service = RedisService()
        redis_service.host = env_config["redis_service"]["host"].replace('{env}', self.__env)
        redis_service.port = env_config["redis_service"]["port"]
        redis_service.passwd = env_config["redis_service"]["passwd"]
        return redis_service

    def __get_codis_service_info(self, env_config):
        codis_service = CodisService()
        codis_service.host = env_config["codis_service"]["host"].replace('{env}', self.__env)
        codis_service.port = env_config["codis_service"]["port"]
        codis_service.passwd = env_config["codis_service"]["passwd"]
        return codis_service

run_config = RunConfig()
