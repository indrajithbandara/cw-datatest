#coding=utf-8  
import urllib  
import urllib2  
import re  
import json  
import time  
import threading  
import itchat  
from itchat.content import *  
   
  
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
headers = { 'User-Agent' : user_agent }  
mylist=[]  
i=0  
  
for page in range(1,20):  
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)  
    try:  
        request = urllib2.Request(url,headers = headers)  
        response = urllib2.urlopen(request)  
        content = response.read().decode('utf-8')  
        pattern = re.compile('<div class="author clearfix">.*?href.*?<img src.*?title=.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<i class="number">.*?</i>',re.S)  
        items = re.findall(pattern,content)  
        for item in items:  
            mytest=item[1].replace('<span>','').replace('</span>','').replace('<br/>','')  
            mylist.append(mytest)  
            #print mytest  
    except urllib2.URLError, e:  
        if hasattr(e,"code"):  
            print e.code  
        if hasattr(e,"reason"):  
            print e.reason  
  
wlist=[]  
def weather(id):  
    try:  
        url = 'https://api.heweather.com/x3/weather?cityid='+str(id)+'&key=84e1b2f93f58433abc6cbc'  
        request = urllib2.Request(url,headers = headers)  
        response = urllib2.urlopen(request)  
        content = response.read()  
        data=json.loads(content)  
        #mydict={}  
        myw=data['HeWeather data service 3.0'][0]['daily_forecast']  
        wlist=[]  
        for i in range(0,7):  
            wdict={}  
            #print myw[i]['date']  
            wdict['date']=myw[i]['date']  
            #print myw[i]['cond']['txt_d']  
            wdict['txt_d']=myw[i]['cond']['txt_d']  
            #print myw[i]['cond']['txt_n']  
            wdict['txt_n']=myw[i]['cond']['txt_n']  
            #print myw[i]['tmp']['max']  
            wdict['max']=myw[i]['tmp']['max']  
            #print myw[i]['tmp']['min']  
            wdict['min']=myw[i]['tmp']['min']  
            #print myw[i]['wind']['dir']  
            wdict['dir']=myw[i]['wind']['dir']  
            #print myw[i]['wind']['sc']  
            wdict['sc']=myw[i]['wind']['sc']  
            wlist.append(wdict)  
        #print wlist  
        return wlist  
    except urllib2.URLError, e:  
        if hasattr(e,"code"):  
            print e.code  
        if hasattr(e,"reason"):  
            print e.reason  
#weather()  
         
          
@itchat.msg_register(TEXT, isGroupChat=True)  
def weather_reply(msg):  
    if msg['Content']==u'天气':  
        if msg['ActualNickName']=='LIAO':  
            a=[]  
            a=weather('CN101210101')  
            itchat.send(u"亲爱的大帅哥：杭州今天%s的天气，白天 %s，晚上 %s ，最高温度%s， 最低温度%s， %s风力等级%s"%(a[0]['date'],a[0]['txt_d'],a[0]['txt_n'],a[0]['max'],a[0]['min'],a[0]['dir'],a[0]['sc']),itchat.get_chatrooms()[0]['UserName'])  
            time.sleep(1)  
            itchat.send(u"亲爱的大帅哥：杭州明天%s的天气，白天 %s，晚上 %s ，最高温度%s， 最低温度%s， %s风力等级%s"%(a[1]['date'],a[1]['txt_d'],a[1]['txt_n'],a[1]['max'],a[1]['min'],a[1]['dir'],a[1]['sc']),itchat.get_chatrooms()[0]['UserName'])  
            #print wlist  
        elif msg['ActualNickName']=='pilipala':  
            c=[]  
            c=weather('CN101280701')  
            itchat.send(u"亲爱的老弟：珠海今天%s的天气，白天 %s，晚上 %s ，最高温度%s， 最低温度%s， %s风力等级%s"%(c[0]['date'],c[0]['txt_d'],c[0]['txt_n'],c[0]['max'],c[0]['min'],c[0]['dir'],c[0]['sc']),itchat.get_chatrooms()[0]['UserName'])  
            time.sleep(1)  
            itchat.send(u"亲爱的老弟珠海：明天%s的天气，白天 %s，晚上 %s ，最高温度%s， 最低温度%s， %s风力等级%s"%(c[1]['date'],c[1]['txt_d'],c[1]['txt_n'],c[1]['max'],c[1]['min'],c[1]['dir'],c[1]['sc']),itchat.get_chatrooms()[0]['UserName'])  
            #wlist=[]  
        else:  
            b=[]  
            b=weather('CN101300404')  
            itchat.send(u"象州今天%s的天气，白天 %s，晚上 %s ，最高温度%s， 最低温度%s， %s风力等级%s"%(b[0]['date'],b[0]['txt_d'],b[0]['txt_n'],b[0]['max'],b[0]['min'],b[0]['dir'],b[0]['sc']),itchat.get_chatrooms()[0]['UserName'])  
            time.sleep(1)  
            itchat.send(u"象州明天%s的天气，白天 %s，晚上 %s ，最高温度%s， 最低温度%s， %s风力等级%s"%(b[1]['date'],b[1]['txt_d'],b[1]['txt_n'],b[1]['max'],b[1]['min'],b[1]['dir'],b[1]['sc']),itchat.get_chatrooms()[0]['UserName'])  
            #print wlist  
    elif msg['Content']==u"笑话":  
        itchat.send(mylist[0],itchat.get_chatrooms()[0]['UserName'])  
        del mylist[0]  
  
    elif msg['isAt']==True:  
        itchat.send(u"我是一只可爱的机器人：可以播报天气预报，也可以讲笑话，回复天气或者笑话",itchat.get_chatrooms()[0]['UserName'])  
          
  
itchat.auto_login()  
  
  
itchat.run() 