# -*- coding:utf8 -*-
import urllib2
import re
import requests
from lxml import etree
import os


def check_save_path(save_path):
    try:
        os.mkdir(save_path)
    except:
        pass


def get_image_name(image_link):
    file_name = os.path.basename(image_link)
    return file_name


def save_image(image_link, save_path):
    file_name = get_image_name(image_link)
    file_path = save_path + "\\" + file_name
    print("准备下载%s" % image_link)
    try:
        file_handler = open(file_path, "wb")
        image_handler = urllib2.urlopen(url=image_link, timeout=5).read()
        file_handler.write(image_handler)
        file_handler.closed()
    except Exception, ex:
        print(ex.message)


def get_image_link_from_web_page(web_page_link):
    image_link_list = []
    print(web_page_link)
    try:
        html_content = urllib2.urlopen(url=web_page_link, timeout=5).read()
        html_tree = etree.HTML(html_content)
        print(str(html_tree))
        link_list = html_tree.xpath('//p/img/@src')
        for link in link_list:
            # print(link)
            if str(link).find("uploadfile"):
                image_link_list.append("http://www.xgyw.cc/" + link)
    except Exception, ex:
        pass
    return image_link_list


def get_page_link_list_from_index_page(base_page_link):
    try:
        html_content = urllib2.urlopen(url=base_page_link, timeout=5).read()
        html_tree = etree.HTML(html_content)
        print(str(html_tree))
        link_tmp_list = html_tree.xpath('//div[@class="page"]/a/@href')
        page_link_list = []
        for link_tmp in link_tmp_list:
            page_link_list.append("http://www.xgyw.cc/" + link_tmp)
        return page_link_list
    except Exception, ex:
        print(ex.message)
        return []


def get_page_title_from_index_page(base_page_link):
    try:
        html_content = urllib2.urlopen(url=base_page_link, timeout=5).read()
        html_tree = etree.HTML(html_content)
        print(str(html_tree))
        page_title_list = html_tree.xpath('//td/div[@class="title"]')
        page_title_tmp = page_title_list[0].text
        print(page_title_tmp)
        return page_title_tmp
    except Exception, ex:
        print(ex.message)
        return ""


def get_image_from_web(base_page_link, save_path):
    check_save_path(save_path)
    page_link_list = get_page_link_list_from_index_page(base_page_link)
    for page_link in page_link_list:
        image_link_list = get_image_link_from_web_page(page_link)
        for image_link in image_link_list:
            save_image(image_link, save_path)


base_page_link = "http://www.xgyw.cc/tuigirl/tuigirl1346.html"
page_title = get_page_title_from_index_page(base_page_link)
if page_title <> "":
    save_path = "N:\\PIC\\" + page_title
else:
    save_path = "N:\\PIC\\other\\"

get_image_from_web(base_page_link, save_path)