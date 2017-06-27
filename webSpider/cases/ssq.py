#-*-coding:utf-8-*-

__author__ = 'huligong'
#双色球
#target_url = http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html

import traceback
from bs4.element import SoupStrainer
import time
from utils import filehelper
from utils.bs4helper import parser
from utils.encoding import smart_str

def get_ssq_list(str_url):
    cur_page_data_list = []
    soup = parser(str_url)
    plist = SoupStrainer("table")
    content = soup.find_all(plist)
    content_table =  content[0]
    trs = content_table.find_all('tr')
    for i,tr in enumerate(trs):
        ssq_info_list = []
        if i >1:
            tds = tr.find_all('td')
            if (len(tds)>5):
                kjrq = tds[0].text #开奖日期
                jh = tds[1].text #期号
                qiu = tds[2]
                ems = qiu.select('em')
                red1 = ems[0].text
                red2 = ems[1].text
                red3 = ems[2].text
                red4 = ems[3].text
                red5 = ems[4].text
                red6 = ems[5].text
                blue1 = ems[6].text
                sales = tds[3].contents[0].string #销售额
                first = tds[4].contents[0].string #一等奖个数
                second = tds[5].contents[0].string #二等奖个数
                distribution = smart_str(tds[4].contents[1].string).replace("(","").replace("..","").replace(")","").strip() #一等奖分布

                ssq_info_list.append(kjrq)
                ssq_info_list.append(jh)
                ssq_info_list.append(red1)
                ssq_info_list.append(red2)
                ssq_info_list.append(red3)
                ssq_info_list.append(red4)
                ssq_info_list.append(red5)
                ssq_info_list.append(red6)
                ssq_info_list.append(blue1)
                ssq_info_list.append(sales)
                ssq_info_list.append(first)
                ssq_info_list.append(second)
                ssq_info_list.append(distribution)
                cur_page_data_list.append(tuple(ssq_info_list))
                #print kjrq,jh,red1,red2,red3,red4,red5,red6,blue1,sales,first,second,distribution

    return cur_page_data_list


def main():
    starttime = time.clock()

    page_size = 72 #72
    title_list = ['开奖日期','期号','红1','红2','红3','红4','红5','红6','蓝','销售额(元)','一等奖','二等奖','一等奖分布地区']
    data_list = []
    for page in range(1,page_size+1):
        data_list.extend(get_ssq_list('http://kaijiang.zhcw.com/zhcw/html/ssq/list_'+str(page)+'.html'))
    filehelper.write_to_csv(title_list,data_list,file_name='lottery_ssq.csv')

    endtime = time.clock()
    print '[All Task Finished in '+str(endtime-starttime)+'s]'


if __name__ == '__main__':
    main()