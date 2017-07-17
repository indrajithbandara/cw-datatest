#!/usr/bin/env python
# -*- coding: utf-8 -*-


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton

@singleton
class Config:

    def __init__(self):
        pass

    def test(self):
        print "test pass"
        pass

@singleton
class DBConn:

    def __init__(self):
        pass

    def getPostConn(self):
        print "test dbconn"
        return "testconn"

config = Config()
config.test()
config.test()
print "#################################"
dbconn=DBConn()
dbconn.getPostConn()
dbconn.getPostConn()
DBConn().getPostConn()

