#-*-coding:utf-8-*-

__author__ = 'huligong'

"""
http://blog.csdn.net/experts.html

http://blog.csdn.net/mobile/experts.html 移动开发

http://blog.csdn.net/web/experts.html Web前端

http://blog.csdn.net/enterprise/experts.html 架构设计

http://blog.csdn.net/code/experts.html 编程语言

http://blog.csdn.net/www/experts.html 互联网

http://blog.csdn.net/database/experts.html 数据库

http://blog.csdn.net/system/experts.html 系统运维

http://blog.csdn.net/cloud/experts.html 云计算

http://blog.csdn.net/software/experts.html 研发管理

http://blog.csdn.net/invite/experts.html 特约专家

http://blog.csdn.net/celebrity/experts.html 行业名家

http://blog.csdn.net/honour/experts.html

获取CSDN上知名博客作者列表
字段包括：注册时间，网名，真实姓名，博客地址，作者归类，博客数量，最近活跃时间
博客标题，简介，博客关注链接，文章分类，文章存档，总访问，积分，排名
统计时间
"""

from bs4.element import SoupStrainer
import time
from utils import filehelper, datehelper, dbhelper
from utils.bs4helper import parser
from utils.encoding import smart_str

def get_author_list(str_url,site_category):
    soup = parser(str_url)
    plist = SoupStrainer(id="experts")
    content = soup.find_all(plist)
    dd_list = content[0].select("dd")

    cur_page_data_list = []

    site = 'blog.csdn.net'
    for dd in dd_list:
        author_info_list = []
        d_a =  dd.select("a")
        url = smart_str(d_a[0]['href'].strip())
        user_name = url.split('net/')[1]
        #real_name = smart_str(d_a[0].text.strip())

        rss = url+'/rss/list'

        #print url
        author_info_list.append(site)
        author_info_list.append(url)
        #author_info_list.append(site_category)
        author_info_list.append(user_name)
        #author_info_list.append(real_name)
        author_info_list.append(rss)
        author_info_list.append(datehelper.now_datetime())
        cur_page_data_list.append(tuple(author_info_list))
       # print author_info_list
    return cur_page_data_list

def main():
    starttime = time.clock()

    index_list = []
    index_list.append(('http://blog.csdn.net/mobile/experts.html','移动开发'))
    index_list.append(('http://blog.csdn.net/web/experts.html','Web前端'))
    index_list.append(('http://blog.csdn.net/enterprise/experts.html','架构设计'))

    data_list = []
    for idx in index_list:
        #print idx[0],idx[1]
        data_list.extend(get_author_list(idx[0],idx[1]))
    #print data_list
    dbhelper.write_to_mysql2('blog_author',data_list)


    endtime = time.clock()
    print '[All Task Finished in '+str(endtime-starttime)+'s]'


if __name__ == '__main__':
    main()