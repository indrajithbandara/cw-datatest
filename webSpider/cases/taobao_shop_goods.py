#-*-coding:utf-8-*-

__author__ = 'huligong'
#淘宝店铺商品信息
#target_url = http://item.taobao.com/item.htm?spm=a1z10.1.4.1.e77b4f&id=14025529535

import traceback
from bs4.element import SoupStrainer
import time
from utils import filehelper
from utils.bs4helper import parser
from utils.encoding import smart_str


def get_goods_data_list(str_url):
    soup = parser(str_url)
    goods_name = smart_str(soup.select('.tb-detail-hd')[0].h3.contents[0].string)
    #print goods_name
    property = soup.select('.tb-property')
    #attributes = soup.select('.attributes')
    #tb-meta
    goods_price = property[0].select('.tb-detail-price')
    j_str_price = goods_price[0].select('strong')[0].text
    #j_promo_price = goods_price[1].select('div')[0]
    #print goods_price
    #print j_str_price
    #print j_promo_price
    sold_out = property[0].select('.tb-sold-out.tb-clearfix')
    evaluate = property[0].select('.tb-evaluate.tb-clearfix')
    print property[0].select('.tb-key.tb-key-sku')

    print evaluate

def main():
    starttime = time.clock()
    get_goods_data_list('http://item.taobao.com/item.htm?spm=a1z10.1.4.1.e77b4f&id=14025529535')
    endtime = time.clock()
    print '[All Task Finished in '+str(endtime-starttime)+'s]'


if __name__ == '__main__':
    main()