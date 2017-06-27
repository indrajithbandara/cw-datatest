#!/usr/bin/env python
#-*-coding:utf-8-*-
#encoding=utf-8
import time
from utils.bs4helper import parser
from utils.encoding import smart_str
from utils.threadhelper import Fetcher

__author__ = 'huligong'

#统计淘宝店铺热销商品共有几页
def getTotalPage(str_url):
    soup = parser(str_url)
    page_info = soup.select('.page-info')[0]
    page_contents = page_info.contents[0]
    totalPage = (str(page_contents)).split('/')[1]
    return int(totalPage)

#统计淘宝店铺热销商品页面的销售总额(单件x销售数量)
def countSale(str_url):
    soup = parser(str_url)
    items = soup.select('.item')
    sale = 0.0 #销售总额
    for item in items:
        amount = 0 #单件商品销售数量
        pricestr = item.select('strong')[0]
        amount_list = item.select('em')
        if len(amount_list) != 0:
            amount = int(amount_list[0].contents[0])
            #price = re.sub(r'</?\w+[^>]*>','',pricestr)
        price_str = smart_str(pricestr.contents[0])
        #price = filter(str.isdigit, price_str)
        price =float(filter(lambda ch: ch in r'0123456789.', price_str))
        sale += round(price*amount,2)
    return sale

#统计淘宝店铺热销商品总的销售额
def getTotalSale(str_url):
    #http://mylafe.taobao.com/search.htm?orderType=_hotsell&pageNum=2
    totalSale = 0.0 #总的销售额
    baseURL = str_url+'/search.htm?orderType=_hotsell'
    totalPage = getTotalPage(baseURL)
    urlList = [baseURL+'&pageNum=%d'%i for i in range(1,totalPage+1)]

    f = Fetcher(threads=len(urlList),func=countSale)
    for url in urlList:
        f.push(url)
    while f.taskleft():
        url,content = f.pop()
        #totalSale += countSale(content)
        totalSale += content
    return totalSale

def main():
    starttime = time.clock()

    taobaoShop = 'http://mylafe.taobao.com' #淘宝店铺地址
    totalSale = getTotalSale(taobaoShop)
    print totalSale
    print '淘宝店铺当前本月销售额:'+ str(totalSale) + '元'

    tmallShop = 'http://mlfjj.tmall.com' #淘宝店铺地址
    totalSale_tmall = getTotalSale(tmallShop)
    print totalSale_tmall
    print '淘宝商城店铺当前本月销售额:'+ str(totalSale_tmall) + '元'

    endtime = time.clock()
    print '[All Task Finished in '+str(endtime-starttime)+'s]'


if __name__ == '__main__':
    main()