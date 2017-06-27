#-*-coding:utf-8-*-
import urllib
import httplib


conn=httplib.HTTPConnection("www.cnblogs.com")
conn.request("GET", "/coderzh/archive/2008/05/13/1194445.html")
r=conn.getresponse()
print r.read() #获取所有内容
print '######################################################################'
target_url = 'http://www.cnblogs.com/coderzh/archive/2008/05/13/1194445.html'
url = urllib.urlopen(target_url)
content = url.read()
print content