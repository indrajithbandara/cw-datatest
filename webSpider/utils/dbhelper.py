#-*-coding:utf-8-*-

import os
import time
import sys
from utils import datehelper, dirhelper

__author__ = 'huligong'

import sqlite3
import traceback

file_root = dirhelper.get_db_folder()

def write_to_sqlite(db_name=None,db_path=None):
    db_path = db_root + datehelper.time_str2()+'.db3'
    print db_path
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('CREATE TABLE foo (o_id INTEGER PRIMARY KEY, fruit VARCHAR(20), veges VARCHAR(30))')
    con.commit()
    cur.execute('INSERT INTO foo (o_id, fruit, veges) VALUES(NULL, "apple", "broccoli")')
    con.commit()
    print cur.lastrowid
    #con.close()
    return db_path

def read_sqlite(db_path,table_name):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('SELECT * FROM '+table_name)
    #con.close()

    # 获取所有结果
    res = cur.fetchall()
    print 'row:', cur.rowcount
    # cur.description是对这个表结构的描述
    print 'desc', cur.description

    return res

def write_to_mysql(table_name,data_list):
    import MySQLdb
    # 连接数据库　
    try:
        conn = MySQLdb.connect(host='localhost',user='root',passwd='mysql',db='test')
        #cursorclass = MySQLdb.cursors.DictCursor
    except Exception, e:
        print e
        sys.exit()

    # 获取cursor对象来进行操作
    cursor = conn.cursor()
    # 创建表
    #sql = "create table if not exists test1(name varchar(128) primary key, age int(4))"
    cursor.execute(sql)
    # 插入数据
    #sql = "insert into test1(name, age) values ('%s', %d)" % ("zhaowei", 23)
    try:
        cursor.execute(sql)
    except Exception, e:
        print e

    sql = "insert into test1(name, age) values ('%s', %d)" % ("张三", 21)
    try:
        cursor.execute(sql)
    except Exception, e:
        print e
    # 插入多条
    sql = "insert into test1(name, age) values (%s, %s)"
    val = (("李四", 24), ("王五", 25), ("洪六", 26))
    try:
        cursor.executemany(sql, val)
    except Exception, e:
        print e

def write_to_mysql2(table_name,data_list):
    import MySQLdb
    # 连接数据库　
    try:
        conn = MySQLdb.connect(host='localhost',user='root',passwd='mysql',db='web_data',charset="utf8",connect_timeout=120)
    except Exception, e:
        print e
        sys.exit()

    cursor = conn.cursor()

    sql = "insert into blog_author(site,url,user_name,rss,add_time) values (%s,%s,%s,%s,now())"
    try:
        cursor.executemany(sql, data_list)
    except Exception, e:
        print e

def write_to_mysql_batch():
    pass

def read_mysql():
    import MySQLdb
    # 连接数据库　
    try:
        conn = MySQLdb.connect(host='localhost',user='root',passwd='mysql',db='test')
    except Exception, e:
        print traceback.format_exc()
        sys.exit()

    # 获取cursor对象来进行操作
    #cursor = conn.cursor()
    cursor = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
    #查询出数据
    sql = "select * from tb_person"
    cursor.execute(sql)
    alldata = cursor.fetchall()
    # 如果有数据返回，就循环输出, alldata是有个二维的列表
    if alldata:
        print alldata
        #for rec in alldata:
        #    print rec[0], rec[1]


    cursor.close()

    conn.close()


def test_sqlite():
    db_path = write_to_sqlite()
    result =  read_sqlite(db_path,'foo')
    for line in result:
       for f in line:
           print f

def test_mysql():
    read_mysql()

def main():
    starttime = time.clock()

    #test_sqlite()
    test_mysql()

    endtime = time.clock()
    print '[All Task Finished in '+str(endtime-starttime)+'s]'


if __name__ == '__main__':
    main()
