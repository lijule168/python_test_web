from lib.util.log_util import l
from lib.common.exception import ServiceException, RedisException, ApiException, DBException
from lib.util.time_util import TimeUtil


class Decorate:

    @staticmethod
    def request_decorate(func):
        def __decorator(*args, **kwargs):
            start_time = TimeUtil.get_timestamp()
            result = ""
            try:
                result = func(*args, **kwargs)
                return result
            except ServiceException as ex:
                raise ex
            except RedisException as ex:
                raise ex
            except ApiException as ex:
                raise ex
            except DBException as ex:
                raise ex
            except Exception as ex:
                l.error(args, kwargs)
                if args.__len__() > 2:
                    raise Exception(
                    "请求接口{0}失败, header:{1}, params:{2}, json:{3}, files:{4}, Exception:{5}".
                        format(args[1] + ", " + args[2], kwargs["headers"] if "headers" in kwargs else None,
                               kwargs["params"] if "params" in kwargs else None,
                               kwargs["json_data"] if "json_data" in kwargs else None,
                               kwargs["files"] if "files" in kwargs else None, ex)
                    )
                else:
                    raise Exception("请求接口失败，参数{0}-{1}".format(args, kwargs))
            finally:
                if args.__len__() > 2:
                    l.info("请求接口{0}-{1} (ms)".format(args[1] + "-" + args[2], TimeUtil.get_timestamp()-start_time))
                else:
                    l.info("请求接口，参数{0}-{1}, {2}".format(args, kwargs, result))

        return __decorator