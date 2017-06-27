#!/usr/bin/env python
#-*-coding:utf-8-*-
#encoding=utf-8
from Queue import Queue
from threading import Lock, Thread
import urllib2
import time


__author__ = 'huligong'


#多线程抓取类
class Fetcher:
    def __init__(self,threads,func):
        self.opener = urllib2.build_opener(urllib2.HTTPHandler)
        self.lock = Lock() #线程锁
        self.q_req = Queue() #任务队列
        self.q_ans = Queue() #完成队列
        self.threads = threads
        self.exec_func = func
        for i in range(threads):
            t = Thread(target=self.threadget)
            #t.setDaemon(True)
            t.start()
        self.running = 0

    def __del__(self): #解构时需等待两个队列完成
        time.sleep(0.5)
        self.q_req.join()
        self.q_ans.join()

    def taskleft(self):
        return self.q_req.qsize()+self.q_ans.qsize()+self.running

    def push(self,req):
        self.q_req.put(req)

    def pop(self):
        return self.q_ans.get()

    def threadget(self):
        while True:
            req = self.q_req.get()
            with self.lock: #要保证该操作的原子性，进入critical area
                self.running += 1
            try:
               #ans = self.opener.open(req).read()
                ans = self.exec_func(req)
            except Exception, what:
                ans =  0.0
                print what
            self.q_ans.put((req,ans))
            with self.lock:
                self.running -= 1
            self.q_req.task_done()
            time.sleep(0.1) # don't spam
