# -*- coding:utf8 -*-
import urllib2, urllib, socket
import re
import requests
from lxml import etree
import os, time

DEFAULT_DOWNLOAD_TIMEOUT = 30


class AppURLopener(urllib.FancyURLopener):
    version = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT)"


def check_save_path(save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)


def get_image_name(image_link):
    file_name = os.path.basename(image_link)
    return file_name


def save_image1(image_link, save_path):
    file_name = get_image_name(image_link)
    file_path = save_path + "\\" + file_name
    print("准备下载{0} 到{1}".format(image_link, file_path))
    try:
        urllib._urlopener = AppURLopener()
        socket.setdefaulttimeout(DEFAULT_DOWNLOAD_TIMEOUT)
        urllib.urlretrieve(url=image_link, filename=save_path)
        return True
    except Exception, ex:
        print(ex.args)
        print("下载文件出错:{0}".format(ex.message))
        return False


def save_image(image_link, save_path):
    file_name = get_image_name(image_link)
    file_path = save_path + "\\" + file_name
    print("准备下载{0} 到{1}".format(image_link, file_path))
    try:
        file_handler = open(file_path, "wb")
        image_handler = urllib2.urlopen(url=image_link, timeout=DEFAULT_DOWNLOAD_TIMEOUT).read()
        file_handler.write(image_handler)
        return True
    except Exception, ex:
        print("下载文件出错:{0}".format(ex.message))
        return False


def get_thumb_picture_link(thumb_page_link):
    try:
        html_content = urllib2.urlopen(url=thumb_page_link, timeout=DEFAULT_DOWNLOAD_TIMEOUT).read()
        html_tree = etree.HTML(html_content)
        # print(str(html_tree))
        link_tmp_list = html_tree.xpath('//div[@class="photo_wrap"]/a[@class="photolst_photo"]/img/@src')
        page_link_list = []
        for link_tmp in link_tmp_list:
            page_link_list.append(link_tmp)
        return page_link_list
    except Exception, ex:
        print(ex.message)
        return []


def download_pictures(album_link, min_page_id, max_page_id, picture_count_per_page, save_path):
    check_save_path(save_path)
    min_page_id = 0
    while min_page_id < max_page_id:
        thumb_page_link = album_link + "?start={0}".format(min_page_id * picture_count_per_page)
        thumb_picture_links = get_thumb_picture_link(thumb_page_link)
        for thumb_picture_link in thumb_picture_links:
            full_picture_link = thumb_picture_link.replace("photo/lthumb", "photo/large")
            save_flag = save_image(image_link=full_picture_link, save_path=save_path)
            if not save_flag:
                full_picture_link = thumb_picture_link.replace("photo/thumb", "photo/photo")
                save_image(image_link=full_picture_link, save_path=save_path)
            time.sleep(1)
        min_page_id += 1
    print("下载完成")


# 设置图片保存的本地文件夹
save_path = "J:\\douban\\gugu"
# 设置相册地址，注意以反斜杠结尾
album_link = "https://www.douban.com/photos/album/1625969357/"
# 设置相册总页数
max_page_id = 11
# 设置每页图片数量，默认为18张
picture_count_per_page = 18

download_pictures(album_link=album_link,
                  min_page_id=1,
                  max_page_id=max_page_id,
                  picture_count_per_page=picture_count_per_page,
                  save_path=save_path)