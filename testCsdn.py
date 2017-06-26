# -*- coding:utf-8 -*-  
import requests  
from bs4 import BeautifulSoup  
import random  
import time  
import MySQLdb  
class csdn():  
    def __init__(self,page):  
        self.page = page  
          
    def get_csdm(self):  
        user_agent=['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36',  
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',  
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',  
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',  
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',  
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',  
        ]  
        headers={  
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',  
        'Accept-Encoding': 'gzip, deflate, sdch',  
        'Accept-Language': 'zh-CN,zh;q=0.8',  
        'User-Agent': user_agent[random.randint(0,5)]  
        }  
  
  
        #获取所有博文链接  
        links = []  
        for i in range(1,page+1):  
            url = 'http://blog.csdn.net/qq1124794084/article/list/'+str(i)  
            r = requests.get(url,headers=headers)  
            html = r.text  
            soup = BeautifulSoup(html)  
            for tag in soup.find('div',id='article_list').find_all('span',class_='link_title'):  
                for href in tag.find_all('a'):  
                    print href.attrs['href']  
                    links.append(href.attrs['href'])  
                      
                      
  
  
        db = MySQLdb.connect("localhost","root",'liao1234','liao',charset='utf8')  
        cursor = db.cursor()  
        sql = "select ip,port from proxies"  
        domains = []  
        try:  
            cursor.execute(sql)  
            results = cursor.fetchall()  
            for row in results:  
                ip = row[0]  
                port = row[1]  
                print u"ip is %s,port is %s"%(ip,port)  
                domian = "http://"+str(row[0])+":"+str(row[1])  
                domains.append(domian)  
        except:  
           print "Error: unable to fecth data"  
  
  
        #设置访问每篇博文最大访问次数  
        base_url = "http://blog.csdn.net"  
        for link in links:  
            url = base_url + link  
            #设置每页最大刷的次数max  
            max = 100  
            min = random.randint(0,max)  
            for i in range(min,max):  
                try:  
                    s = random.randint(0,len(domains)-1)  
                    proxies = { "http": domains[s], "https": domains[s], }  
                    r = requests.get(url,headers=headers,proxies=proxies,timeout=5)  
                    time.sleep(0.1)  
                except:  
                    print "error return again"  
            print u"刷完了%s"%url  
  
  
        db.close()  
          
if __name__ = '__main__':  
    test = csdn()  
    test.get_csdn(5)  