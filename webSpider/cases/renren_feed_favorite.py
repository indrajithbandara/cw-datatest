#-*-coding:utf-8-*-
#note:人人网特别关注好友新鲜事
#tech: BeautifulSoup

__author__ = 'huligong'

from bs4 import BeautifulSoup
import urllib,urllib2,cookielib
from utils.encoding import smart_str


#人人网特别关注好友新鲜事
def feed_favorite(parser):
    article_list = parser.find_all('article')
    for my_article in article_list:
        state = []
        all_content = ''
        for my_tag in my_article.h3.contents:
            factor = my_tag.string
            if factor != None:
                factor = factor.strip(u'\r\n')
                factor = factor.strip(u'\n')
                factor = factor.replace(u'\n','')
                factor = factor.strip()
                state.append(smart_str(factor))
        content = my_article.select('.content')
        duration = my_article.select('.duration')
        if content:
            block_quote = content[0].select('blockquote')
            if block_quote:
                content_detail = smart_str(block_quote[0].contents[0].string)
                state.append(content_detail)
        if duration:
            state.append(smart_str(duration[0].string))
        print ''.join(state)


def main():
    myCookie = urllib2.HTTPCookieProcessor(cookielib.CookieJar());
    opener = urllib2.build_opener(myCookie)

    post_data = {
        'email':'xxxx',
        'password':'xxxx',
        #'origURL':'http://www.renren.com/Home.do',
        #'origURL':'http://www.renren.com/feedretrieve2.do',#renren 新鲜事-热点内容
        'origURL':'http://www.renren.com/feedfavorite2.do', #renren特别关注好友新鲜事
        'domain':'renren.com'
    }

    req = urllib2.Request('http://www.renren.com/PLogin.do', urllib.urlencode(post_data))
    html_src = opener.open(req).read()
    parser = BeautifulSoup(html_src,from_encoding='utf-8')
    #article_list = parser.find('div','feed-list').findAll('article')
    feed_favorite(parser)

if __name__ == '__main__':
    main()