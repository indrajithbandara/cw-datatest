#!/usr/bin/env python
#-*-coding:utf-8-*-
#encoding=utf-8
import cookielib
from gzip import GzipFile
from StringIO import StringIO
import socket
import urllib
import urllib2
import zlib
from bs4 import BeautifulSoup
import time

__author__ = 'huligong'

socket.setdefaulttimeout(30) #设置10秒后连接超时

#gzip/deflate支持
class ContentEncodingProcessor(urllib2.BaseHandler):
    """A handler to add gzip capabilities to urllib2 requests """

    # add headers to requests
    def http_request(self, req):
        req.add_header("Accept-Encoding", "gzip, deflate")
        return req

    # decode
    def http_response(self, req, resp):
        old_resp = resp
        # gzip
        if resp.headers.get("content-encoding") == "gzip":
            gz = GzipFile(
                fileobj=StringIO(resp.read()),
                mode="r"
            )
            resp = urllib2.addinfourl(gz, old_resp.headers, old_resp.url, old_resp.code)
            resp.msg = old_resp.msg
            # deflate
        if resp.headers.get("content-encoding") == "deflate":
            gz = StringIO( deflate(resp.read()) )
            resp = urllib2.addinfourl(gz, old_resp.headers, old_resp.url, old_resp.code)  # 'class to add info() and
            resp.msg = old_resp.msg
        return resp

# deflate support
def deflate(data):   # zlib only provides the zlib compress format, not the deflate format;
    try:               # so on top of all there's this workaround:
        return zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        return zlib.decompress(data)


proxy_type = 'http'
proxy_url = 'http://218.108.168.166:80'

#构造请求参数
def make_req(str_url,browser=True,post_data=None):
    req = urllib2.Request(str_url)
    #伪装成浏览器访问
    if browser:
        req.add_header( 'User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')

    #通过post方式提交参数
    if post_data:
        req.add_data(post_data)
    return req

def parser(str_url,proxy_support=[],gzip_support=True,cookie_support=False,browser=True,post_data=None,from_encoding=None):
    starttime = time.clock()
    print str_url
    req = make_req(str_url,browser,post_data)
    hander_classes = []
    if proxy_support:
        #使用代理服务器
        proxy_handler = urllib2.ProxyHandler(proxy_support)
        hander_classes.append(proxy_handler)
    if gzip_support:
        #gzip支持
        hander_classes.append(ContentEncodingProcessor)

    if cookie_support:
        #获取一个保存cookie的对象
        cj = cookielib.LWPCookieJar()
        #将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
        cookie_handler = urllib2.HTTPCookieProcessor(cj)
        hander_classes.append(cookie_handler)

    #设置HTTPHandler用于处理http的URL的打开
    hander_classes.append(urllib2.HTTPHandler)

    #创建一个opener，保存cookie,gzip,proxy等http处理器
    opener = urllib2.build_opener(*hander_classes)
    #将包含了cookie、http处理器、http的handler的资源和urllib2对象板顶在一起
    urllib2.install_opener(opener)
    #直接用opener打开网页，如果服务器支持gzip/defalte则自动解压缩
    content = opener.open(req).read()
    if from_encoding:
        soup = BeautifulSoup(content,from_encoding=from_encoding)
    else:
        soup = BeautifulSoup(content)
    endtime = time.clock()
    print '[Parser Finished in '+str(endtime-starttime)+'s]'
    return soup


def main():
    login_data = {}
    #post_data = urllib.urlencode(login_data)
    proxy_support = {'http': 'http://218.108.168.166:80'}
    print parser('http://www.taobao.com',proxy_support=proxy_support)

if __name__ == '__main__':
    main()