#! /usr/bin/env python
# coding=utf-8

import httplib 
import time 
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

conn = httplib.HTTPConnection("api.showji.com") 
tels = []

def q(tel_prefix,tel):
	if tel_prefix in tels:
		return
	timeStr = str(long(time.time()*1000))
	target_path = "/Locating/www.show.ji.c.o.m.aspx?m="+tel+"&output=json&timestamp="+timeStr
	conn.request("GET", target_path)  
	r1 = conn.getresponse()  
	jsonString = r1.read()
	#print jsonString #{"Mobile":"17751511358","QueryResult":"True","TO":"中国电信","Corp":"中国电信","Province":"江苏","City":"无锡","AreaCode":"0510","PostCode":"214000","VNO":"","Card":""}
	jsonObj = json.loads(jsonString, encoding="utf-8")
	if (jsonObj['QueryResult'] == 'True') and (jsonObj['City'] != '') :
		tels.append(tel_prefix)
		#print jsonString
		content=tel_prefix+','+jsonObj['Province']+' '+jsonObj['City']+','+jsonObj['Corp']+','+jsonObj['AreaCode']+','+jsonObj['PostCode']+','+'CT'
		output = open('tel_data.txt', 'a')
		output.write(content+'\n')
		output.close()
		print content

if __name__ == '__main__':
	print 'start ...'
	for i in range(1770000, 1779999):
		if i%10 == 0:
			time.sleep(30)
		tel = str(i)+'1000'
		q(str(i),tel)
	print 'end.'