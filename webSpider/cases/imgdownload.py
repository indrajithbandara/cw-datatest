#-*-coding:utf-8-*-
#python27
import os
import traceback

import urllib,urllib2
import threading
from time import sleep,ctime
#from html import parser
import HTMLParser
import time
from utils import dirhelper
from utils.encoding import smart_str

file_root = dirhelper.get_image_folder()

def down_jpg( file_path,file_name ="default.jpg"):
    try:
        web = urllib.urlopen( file_path)
        #print("访问网络文件"+file_path+"\n")
        jpg = web.read()
        #print("保存文件"+file_root+file_name+"\n")
        try:
            file = open(file_root+file_name,"wb")
            file.write(jpg)
            file.close()
            return
        except IOError:
            print traceback.format_exc()
            return
    except Exception:
        print traceback.format_exc()
        return


def down_jpg_mutithread(file_path_list):
    print("共有%d个文件需要下载"%len(file_path_list))
    for file in file_path_list:
        print( file )
    print("开始多线程下载")
    task_threads=[] #存储线程
    count=1
    for file in file_path_list:
        t= threading.Thread(target=down_jpg,args=(file,"%d.jpg"%count) )
        count=count+1
        task_threads.append(t)
    for task in task_threads:
        task.start()
    for task in task_threads:
        task.join() #等待所有线程结束
    print("线程结束")

class ParserLinks( HTMLParser.HTMLParser):
    file_list=[]
    def handle_starttag(self,tag,attrs):
        if tag == 'img':
            for name,value in attrs:
                if name == 'src':
                    print( value)
                    self.file_list.append(value)
    def get_file_list(self):
        return self.file_list


def main(str_url):
    parserLinks = ParserLinks()
    web = urllib.urlopen(str_url)
    for context in web.readlines():
        _str = smart_str(context).decode('utf-8')
        try:
            parserLinks.feed(_str)
        except HTMLParser.HTMLParseError:
            print traceback.format_exc()
            pass
    web.close()
    image_list= parserLinks.get_file_list()
    down_jpg_mutithread(image_list)

if __name__ == '__main__':
    starttime = time.clock()

    #str_url="http://www.baidu.com/" #要抓去的网页链接
    str_url="http://hi.baidu.com/%C7%A7%D2%B6%CF%C4%D1%A9/blog/item/0f119f5404428148d109062a.html"
    main(str_url)

    endtime = time.clock()
    print '[All Task Finished in '+str(endtime-starttime)+'s]'