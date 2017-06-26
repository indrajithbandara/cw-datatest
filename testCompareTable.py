# -*- coding:utf-8 -*-  
import xlrd  
import sys  
import re  
import json  
  
dict1={}  
dict2={}  
mylist=[u'系统运维管理',u'安全管理机构',u'安全管理制度',u'人员安全管理',u'网络安全',u'物理安全',u'网络安全',u'主机安全',u'应用安全',u"网络安全",u"主机安全",u"主机安全",u'系统建设管理']  
def check():  
    data=xlrd.open_workbook('test.xls')  
    for i in range(0,13):  
        print u"第%s个表格"%(i+1)  
        print mylist[i]  
        print "-"*60  
        try:  
            table=data.sheets()[i]  
        except IndexError,e:  
            break      
        nrows=table.nrows  
        count=1  
        if i<5:  
            m=10  
        else:  
            m=16  
        for j in range(m,nrows):  
            cell_1=table.cell(j,2).value  
            #print cell_1,  
            cell_2=table.cell(j,3).value  
            nu=re.split(r'\)',cell_2)  
            num=re.split(r'\）',nu[0])  
            if num is not None:  
                #print num[0],  
                pass  
            else:  
                print u"没有标记序号"  
            try:  
                if j<nrows:  
                    if table.cell(j,2).value==table.cell(j+1,2).value:  
                        count+=1  
                    else:  
                        print u"检查项【%s】共有【%s】项"%(table.cell(j,2).value,count)  
                        key=mylist[i]+table.cell(j,2).value  
                        dict1[key]=count  
                        count=1  
                else:  
                    count+=1  
                    print u"检查项【%s】共有【%s】项"%(table.cell(j,2).value,count)  
                    key=mylist[i]+table.cell(j,2).value  
                    dict1[key]=count  
                  
            except IndexError,e:  
                #count+=1  
                print u"检查项【%s】共有【%s】项"%(table.cell(j,2).value,count)  
                key=mylist[i]+table.cell(j,2).value  
                dict1[key]=count  
        print "-"*60  
    print json.dumps(dict1, encoding='UTF-8', ensure_ascii=False)  
    print u"完成excel表格读取-Thanks"  
  
def ASGcheck(filename):  
    data=xlrd.open_workbook(filename)  
    table=data.sheets()[0]  
    print "-"*60    
    nrows=table.nrows  
    count=1  
    for j in range(1,nrows):  
        cell_1=table.cell(j,2).value  
        #print cell_1,  
        cell_2=table.cell(j,3).value  
        nu=re.split(r'\)',cell_2)  
        num=re.split(r'\）',nu[0])  
        if num is not None:  
            #print num[0],  
            pass  
        else:  
            print u"没有标记序号"  
        try:  
            if j<nrows:  
                if table.cell(j,3).value==table.cell(j+1,3).value:  
                    count+=1  
                else:  
                    print u"安全层面【%s】检查项【%s】共有【%s】项"%(table.cell(j,2).value,table.cell(j,3).value,count)  
                    key=table.cell(j,2).value+table.cell(j,3).value  
                    dict2[key]=count  
                    count=1  
            else:  
                count+=1  
                print u"安全层面【%s】检查项【%s】共有【%s】项"%(table.cell(j,2).value,table.cell(j,3).value,count)  
                key=table.cell(j,2).value+table.cell(j,3).value  
                dict2[key]=count  
              
        except IndexError,e:  
            #count+=1  
            print u"安全层面【%s】检查项【%s】共有【%s】项"%(table.cell(j,2).value,table.cell(j,3).value,count)  
            key=table.cell(j,2).value+table.cell(j,3).value  
            dict2[key]=count  
    #print json.dumps(dict2, encoding='UTF-8', ensure_ascii=False)  
    print "-"*60  
def standard():  
    choiceA=raw_input(u"请输入A的等级：A2，A3，A4")  
    choiceS=raw_input(u"请输入S的等级：S2，S3，S4")  
    choiceG=raw_input(u"请输入G的等级：G2，G3，G4")  
    Aname=str(choiceA)+".xlsx"  
    Sname=str(choiceS)+".xlsx"  
    Gname=str(choiceG)+".xlsx"  
    check()  
    
    def compare():  
        print "*"*60  
        for key in dict2:  
            try:  
                if dict2[key]!=dict1[key]:  
                    print u"存在异常项"  
                    print u"从程序中导出的检查项【%s】共有%s项"%(key,json.dumps(dict1[key], encoding='UTF-8', ensure_ascii=False))  
                    print u"从分支查询的检查项【%s】共有%s项"%(key,json.dumps(dict2[key], encoding='UTF-8', ensure_ascii=False))  
                else:  
                    pass  
             
            except KeyError,e:  
                print u"分支中的检查项【%s】共有%s项"%(key,json.dumps(dict2[key], encoding='UTF-8', ensure_ascii=False)),  
                print u"程序中没有查询到该项"  
  
  
    #比较分支结果和程序导出的结果     
    ASGcheck(Aname)  
    compare()  
    ASGcheck(Sname)  
    compare()  
    ASGcheck(Gname)  
    compare()  
standard()  
#ASGcheck('S3.xlsx') 