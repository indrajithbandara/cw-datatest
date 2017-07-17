from apscheduler.scheduler import Scheduler
import os
import sys
import time
import MySQLdb
import ConfigParser
import Logger

def main():

    logger = Logger.Logger(logname='flowstat.log', loglevel=1, logger='flowstat').getlog()

    try:
        cf = ConfigParser.ConfigParser()
        cf.read('./flowstat.conf')

        filterNet1 = cf.get('packet', 'filterNet1')
        filterNet2 = cf.get('packet', 'filterNet2')
        packetFile = cf.get('packet', 'packetFile')

        db_host = cf.get('db', 'host')
        db_user = cf.get('db', 'user')
        db_passwd = cf.get('db', 'passwd')
        db_dbname = cf.get('db', 'dbname')

        conn = MySQLdb.connect(host=db_host, user=db_user, passwd=db_passwd, db=db_dbname, port=3306)

        os.system('nohup ./capturePacket.sh ' + filterNet1 + ' ' + filterNet2 + ' ' + packetFile + ' &')
    except Exception, e:
        logger.error(e)
        sys.exit(1)


    sched = Scheduler(daemonic = False)
    @sched.cron_schedule(day_of_week='0-4', hour='*', minute='0-59', second='*/60')
    def packagestat_job():
        logger.debug('stat package' + ' ' + time.strftime("%Y-%m-%d %H:%M:%S"))
        try:
            fos = open(packetFile, 'r+')
            lines = fos.readlines()
            values = []
            for line in lines:
                arr = line.split(',')
                if len(arr) > 4:
                    values.append((arr[0].strip(), arr[2].strip(), arr[3].strip(), arr[4].strip()))

            if len(values) > 0:
                cur = conn.cursor()
                cur.executemany('insert into tbpk_packet(TimesMacs, LengthIps, Seq, Ack) values(%s,%s,%s,%s)', values)
                conn.commit()
                cur.close()

            fos.truncate(0)
            fos.close()
        except Exception, e3:
            Logger.error(e3)


    sched.start()

    while 1:
        time.sleep(60)

    conn.close()

if __name__ == '__main__':
    main()

shell脚本
#!/bin/sh
tcpdump -i eth0 -l >> *.txt