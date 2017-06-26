# -*- coding: utf-8 -*-  
import time  
import os  
import os.path  
import re  
import unittest  
import HTMLTestRunner  
import shutil  
shutil.copyfile("setting.ini","../setting.ini")  
casepaths = []  
os.makedirs('test-case')  
casepath='test-case'  
def createsuite():  
    testunit = unittest.TestSuite()  
    #discover方法定义  
    discover = unittest.defaultTestLoader.discover(  
    casepath,  
    pattern = 'case*.py',  
    top_level_dir= casepath  
    )  
    for test_suite in discover:  
        for test_case in test_suite:  
            testunit.addTest(test_case)  
    print testunit  
    return testunit  
for parent,dirnames,filenames in os.walk('.'):  
  
    for filename in filenames:  
        #print "parent is:" + parent  
        #print "filename is:" + filename  
        path=os.path.join(parent,filename)  
        #正则判断是否为测试用例  
        match = re.match('case', filename)  
        if match:  
            
            casepaths.append(parent)  
            oldfile = parent+"/"+filename  
            try:  
                shutil.copy(oldfile,'test-case')  
            except shutil.Error,e:  
                continue  
                print u"出现shutil.Error"  
            print u"正在读取测试用例:%s%s" %(parent,filename)  
  
            
  
#定义报告存放目录,支持相对路径  
now = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))  
filename = now+'report.html'  
fp = file(filename,'wb')  
runner = HTMLTestRunner.HTMLTestRunner(  
stream = fp,  
title  = u'自动化测试报告',  
description = u'用例执行情况'  
)  
alltestnames = createsuite()  
print u"正在执行测试用例，请等待！"  
runner.run(alltestnames)  
  
print u"正在清理缓存文件"  
shutil.rmtree('test-case')  
os.remove('../setting.ini')  
print u"缓存文件清理完成"  
print u"完成所有测试用例执行任务"  