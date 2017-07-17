import sys, urllib2, urllib,cookielib
import re
cookie = cookielib.LWPCookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)
url='http://entry.mail.126.com/cgi/login?hid=10010102&lightweight=1&language=0&style=11'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
values = {'bCookie' : '',
  'domain' : '126.com',
  'enter.x' : '登 录',
  'language':'0',
  'pass':'#####',
  'style':'11',
  'user':'guijia8427'}
data = urllib.urlencode(values)
req = urllib2.Request(url, data ,headers)
response = urllib2.urlopen(req)
the_page = response.read()
sor= re.compile(r'sid=(.+)&funcid')
s=sor.findall(the_page)
url2='http://tg1a3.mail.126.com/coremail/fcg/ldapapp?funcid=mails&sid='+s[0]+'&fid=1'
g=opener.open(url2)
data2=g.read()
file=open('126.html','w')
file.write(data2)
file.close()