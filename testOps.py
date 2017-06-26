#-*- encoding:utf-8 -*-  
#!/usr/bin/env python  
# name IsOpen.py  
import os  
import socket  
import time  
import smtplib    
from email.mime.text import MIMEText  
  
mailto_list=["872766492@qq.com"]   
mail_host="smtp.qq.com"  #设置服务器  
mail_user="1124794084"    #用户名  
mail_pass="密码"   #口令   
mail_postfix="qq.com"  #发件箱的后缀  
    
def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容  
    me="升级服务器报告"+"<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示  
    msg = MIMEText(content,_subtype='html',_charset='gb2312')    #创建一个实例，这里设置为html格式邮件  
    msg['Subject'] = sub    #设置主题  
    msg['From'] = me    
    msg['To'] = ";".join(to_list)    
    try:    
        s = smtplib.SMTP()    
        s.connect(mail_host)  #连接smtp服务器  
        s.login(mail_user,mail_pass)  #登陆服务器  
        s.sendmail(me, to_list, msg.as_string())  #发送邮件  
        s.close()    
        return True    
    except Exception, e:    
        print str(e)    
        return False  
  
  
def IsOpen(ip,port,flag):  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
    try:  
        s.connect((ip,int(port)))  
        s.shutdown(2)  
        print '%d is open' % port  
        return True  
    except:  
        print '%d is down' % port    
        return False  
      
if __name__ == '__main__':  
    while(1>0):  
        flag=1  
        IsOpen('127.0.0.1',9906)  
        time.sleep(60)  
        flag=IsOpen('127.0.0.1',9906)  
        print flag  
        if flag==False:  
            send_mail(mailto_list,"XX升级服务器监测异常","error")  
            time.sleep(1800)  
  
#设置一分钟监测一次，如果发现端口9906消失则发送邮件报告，设置延迟为半小时，避免一直重复发送邮件  