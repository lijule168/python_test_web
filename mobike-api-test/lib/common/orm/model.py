#!/usr/bin/python

from lib.common.orm.field import Field
from lib.common.mysql_helper import MysqlHelper

class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        table_name = attrs.get('__table__', None) or name
        if table_name == "Model":
            return type.__new__(cls, name, bases, attrs)
        db_conn = attrs.get('__db_conn__', None)
        # if db_conn is None:
        #     raise Exception("Need to define __db_conn__ variable in model")
        mappings = dict()
        fields = []
        primary_key = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
                if v.primary_key:
                    if primary_key:
                        pass
                        #TODO
                        #raise StandardError('Duplicate primary key for field: %s' %k)
                    primary_key = k
                else:
                    fields.append(k)

        #if not primary_key:
        #    raise StandardError('Primary key is nor founnd')

        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda f:'`%s`' %f, fields))

        attrs["__mappings__"] = mappings
        attrs["__table__"] = table_name
        attrs["__primary_key__"] = primary_key
        attrs["__field__"] =  fields
        attrs["__db_conn__"] = db_conn
        # attrs['__select__'] = 'select `%s`, %s from `%s` ' % (primary_key, ', '.join(escaped_fields), table_name)
        # attrs['__insert__'] = 'insert into  `%s` (%s, `%s`) values(%s)' % (
        #     table_name, ', '.join(escaped_fields), primary_key, ModelMetaClass.create_args_string(len(escaped_fields) + 1))
        # attrs['__update__'] = 'update `%s` set `%s` where `%s` = ?' % (
        #     table_name, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primary_key)
        # attrs['__delete__'] = 'delete from  `%s` where `%s`=?' % (table_name, primary_key)

        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__ = ModelMetaClass

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)
        self.__where_clause = ""
        self.__order_clause = ""

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.items():
            if k =='_Model__where_clause' or k == '_Model__order_clause':
                continue
            try:
                value = getattr(self, k)
            except AttributeError:
                continue
            except:
                value = getattr(self, k, None)
            fields.append(k)
            params.append('%s')
            args.append(v)
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        db_helper = MysqlHelper(self.__db_conn__)
        result = db_helper.execute_non_query_cmd(sql, args)
        return result

    def where(self, **kwargs):
        clause_list = []
        for key, item in kwargs.items():
            clause_list.append(str(key) + "=" + "'"+str(item)+"'")
        self.__where_clause =  ' where ' + ' and '.join([item for item in clause_list]) if len(clause_list) > 0 else ''
        return self

    def in_clause(self, in_clause):
        if self.__where_clause:
            self.__where_clause = self.__where_clause + " and " + in_clause
        else:
            self.__where_clause = " where {0}".format(in_clause)
        return self

    def like(self, **kwargs):
        clause_list = []
        for key, item in kwargs.items():
            clause_list.append(str(key) + " like " + "'"+str(item)+"'")
        self.__where_clause =  ' where ' + ' and '.join([item for item in clause_list]) if len(clause_list) > 0 else ''
        return self

    def order_by(self, **kwargs):
        if kwargs.__len__() == 0:
            self.__order_clause = ""
            return self
        self.__order_clause = " order by"
        for key, item in kwargs.items():
            if item:
                sorting = "asc"
            else:
                sorting = "desc"
            self.__order_clause = self.__order_clause + "  {0} {1},".format(key, sorting)
        self.__order_clause = self.__order_clause[0:len(self.__order_clause)-1]
        return self

    def insert(self, **kwargs):
        cols, args = zip(*kwargs.items())
        sql = 'INSERT INTO %s (%s) VALUES (%s)' % (self.__table__, ','.join(['%s'% col for col in cols]),
                                                   ','.join(['%s'] * len(kwargs)))
        db_helper = MysqlHelper(self.__db_conn__)
        result = db_helper.execute_non_query_cmd(sql, args)
        return result

    def select(self, *args):
        if len(args) == 0:
            self.__select_sql =  'select %s from `%s` ' % (', '.join(self.__field__), self.__table__)
        else:
            self.__select_sql = 'select %s from `%s` ' % (', '.join(args), self.__table__)
        if self.__where_clause:
            self.__select_sql = self.__select_sql + self.__where_clause
        if self.__order_clause:
            self.__select_sql =  self.__select_sql + self.__order_clause
        db_helper = MysqlHelper(self.__db_conn__)

        try:
            result = db_helper.execute_query_records(self.__select_sql)
            return result
        finally:
            self.__select_sql = None
            self.__where_clause = None
            self.__order_clause = None

    def update(self, **kwargs):
        # clause_list = []
        # for key, value in kwargs.items():
        #     clause_list.append(str(key) + "=" + str(value))
        # if len(clause_list) == 0:
        #     return
        cols, args = zip(*kwargs.items())
        #sql = 'UPDATE %s SET %s' % (self.__table__, ' , '.join([item for item in clause_list]))
        sql = 'UPDATE %s SET %s' % (self.__table__, ','.join(['%s={}'% col for col in cols]))
        sql = sql.replace('{}', "%s")
        if self.__where_clause:
            sql = sql + self.__where_clause
        db_helper = MysqlHelper(self.__db_conn__)
        try:
            result = db_helper.execute_non_query_cmd(sql, args)
            return result
        finally:
            self.__where_clause = None

    def delete(self):
        sql = "DELETE FROM %s " % (self.__table__)
        if self.__where_clause:
            sql = sql + self.__where_clause
        db_helper = MysqlHelper(self.__db_conn__)
        try:
            result = db_helper.execute_non_query_cmd(sql)
            return result
        finally:
            self.__where_clause = None

    def execute_non_query(self, sql, args):
        '''

        :param sql:
        :param args:
        :return:
        '''
        db_helper = MysqlHelper(self.__db_conn__)
        result = db_helper.execute_non_query_cmd(sql, args)
        return result

    def execute_query(self, sql, args):
        '''

        :param sql:
        :param args:
        :return:
        '''
        db_helper = MysqlHelper(self.__db_conn__)
        result = db_helper.execute_query_records(sql, args)
        return result
