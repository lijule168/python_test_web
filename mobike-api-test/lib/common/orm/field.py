#!/usr/bin/python
#-*- coding:utf-8 -*-

class Field(object):
    def __init__(self, name, column_type, primary_key, default, comment):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default
        self.comment = comment

    def __str__(self):
        return ('<%s, %s: %s>' %(self.__class__.__name__, self.column_type, self.name))

class StringField(Field):
    def __init__(self, name=None, primary_key=False, default=None, column_type='varchar(100)', comment=''):
        super(StringField, self).__init__(name, column_type, primary_key, default, comment)


class BooleanField(Field):
    def __init__(self, name=None, default=None, comment=''):
        super(BooleanField, self).__init__(name, 'boolean', False, default, comment)

class BitField(Field):
    def __init__(self, name=None, default=None, comment=''):
        super(BitField, self).__init__(name, 'bit', False, default, comment)


class IntegerField(Field):
    def __init__(self, name=None, primary_key=False, default=0, comment=''):
        super(IntegerField, self).__init__(name, 'bigint', primary_key, default, comment)

class FloatField(Field):
    def __init__(self, name=None, primary_key=False, default=0.0, comment=''):
        super(FloatField, self).__init__(name, 'real', primary_key, default, comment)


class TextField(Field):
    def __init__(self, name=None, default=None, comment=''):
        super(TextField, self).__init__(name, 'Text', False, default, comment)

class TimestampField(Field):
    def __init__(self, name=None, default=None, comment=''):
        super(TimestampField, self).__init__(name, 'timestamp', False, default, comment)

class DateTimeField(Field):
    def __init__(self, name=None, default=None, comment=''):
        super(DateTimeField, self).__init__(name, 'datetime', False, default, comment)

class DateField(Field):
    def __init__(self, name=None, default=None, comment=''):
        super(DateField, self).__init__(name, 'date', False, default, comment)

class DecimalField(Field):
    def __init__(self, name=None, default=None, comment=''):
        super(DecimalField, self).__init__(name, 'decimal', False, default, comment)

class DoubleField(Field):
    def __init__(self, name=None, default=None, comment=''):
        super(DoubleField, self).__init__(name, 'double', False, default, comment)

class BlobField(Field):
    def __init__(self, name=None, default=None, comment=''):
        super(BlobField, self).__init__(name, 'blob', False, default, comment)