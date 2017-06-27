#-*-coding:utf-8-*-
__author__ = 'huligong'
#python抓取google搜索url

import sys
import urllib2
import simplejson

def search_by_google(search_key=None,page_index=0):
    if search_key is None:
        return None
    url = ('https://ajax.googleapis.com/ajax/services/search/web''?v=1.0&q=%s&rsz=8&start=%s') % (search_key,page_index)
    info = dict({})
    try:
        request = urllib2.Request(url, None, {'Referer': 'http://www.google.com'})
        response = urllib2.urlopen(request)

        # Process the JSON string.
        return_json = simplejson.load(response)
        responseData = return_json['responseData']
        responseDetails = return_json['responseDetails']
        responseStatus = return_json['responseStatus']

        results = responseData['results']
        cursor  = responseData['cursor']
        print results,cursor
    except Exception,e:
        print e
    #time.sleep(5)
    #continue

    for result in results:
        GsearchResultClass = result['GsearchResultClass']
        unescapedUrl = result['unescapedUrl']
        url = result['url']
        visibleUrl = result['visibleUrl']
        cacheUrl = result['cacheUrl']
        title = result['title']
        titleNoFormatting = result['titleNoFormatting']
        content = result['content']
        print titleNoFormatting,url

    pages = cursor['pages']
    moreResultsUrl = cursor['moreResultsUrl']
    estimatedResultCount = cursor['estimatedResultCount']
    searchResultTime = cursor['searchResultTime']
    resultCount = cursor['resultCount']
    currentPageIndex = cursor['currentPageIndex']


def main():
    search_key = 'Java'
    search_by_google(search_key,0)

if __name__ == '__main__':
    main()
