#-*-coding:utf-8-*-

__author__ = 'huligong'
#图书计算机与互联网销售榜Top 100
#target_url = http://www.360buy.com/booktop-1-2-3287-1.html

import traceback
from bs4.element import SoupStrainer
import time
from utils import filehelper
from utils.bs4helper import parser
from utils.encoding import smart_str

def get_book_list(str_url):
    soup = parser(str_url)
    plist = SoupStrainer(id="plist")
    content = soup.find_all(plist)
    items = soup.select('.item')
    cur_page_data_list = []
    for item in items:
        book_info_list = []
        index = smart_str(item.select('.index')[0].contents[0].string) #图书排行

        p_name = item.select('.p-name')[0].contents[0]
        book_url = smart_str(p_name['href']) #图书链接地址
        book_name = smart_str(p_name.text) #图书名称

        book_info = item.select('.p-info')
        book_publisher_auther = book_info[0]

        book_p_a_len =  len(list(book_publisher_auther.select('a')))
        book_auther = '' #图书作者
        book_trans_auther = '' #图书译者
        book_publisher = '' #图书出版社
        if book_p_a_len == 2:
            book_auther = smart_str(book_publisher_auther.select('a')[1].text)
            book_publisher = smart_str(book_publisher_auther.select('a')[1].text)
        elif book_p_a_len == 1:
            book_auther = ''
            book_publisher = smart_str(book_publisher_auther.select('a')[0].text)
        elif book_p_a_len == 3:
           book_auther =  smart_str(book_publisher_auther.select('a')[0].text)
           book_trans_auther = smart_str(book_publisher_auther.select('a')[1].text)
           book_publisher = smart_str(book_publisher_auther.select('a')[2].text)

        book_img = smart_str(item.select('.p-img.bookimg')[0].img['src'])

        book_prices = book_info[1]
        del_price = (smart_str(book_prices.select('del')[0].text)).replace('￥','') #定价
        jd_price = (smart_str(book_prices.select('span')[0].text)).replace('￥','') #京东价

        #print index,book_name,book_url
        #print book_auther,book_trans_auther,book_publisher
        #print del_price,jd_price
        #print book_img
        #print '|'.join(book_info_list)

        book_info_list.append(index)
        book_info_list.append(book_name)
        book_info_list.append(book_img)
        book_info_list.append(book_url)
        book_info_list.append(book_auther)
        book_info_list.append(book_trans_auther)
        book_info_list.append(book_publisher)
        book_info_list.append(del_price)
        book_info_list.append(jd_price)
        cur_page_data_list.append(tuple(book_info_list))
    return cur_page_data_list


def main():
    starttime = time.clock()

    page_size = 5
    title_list = ['图书排行','书名','缩略图地址','图书地址','作者','译者','出版社','定价','京东价']
    data_list = []
    for page in range(1,page_size+1):
        data_list.extend(get_book_list('http://www.360buy.com/booktop-1-2-3287-'+str(page)+'.html'))
    filehelper.write_to_csv(title_list,data_list,file_name='360buy_booktop100_computer.csv')

    endtime = time.clock()
    print '[All Task Finished in '+str(endtime-starttime)+'s]'


if __name__ == '__main__':
    main()