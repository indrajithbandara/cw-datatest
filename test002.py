# -*- coding:utf-8 -*-  
import json  
import xlwt  
  
fp = file('vul_db.json','r')  
vul = json.loads(fp.read())  
gk = xlwt.Workbook()  
table = gk.add_sheet(u'信息表格',cell_overwrite_ok=True)  
  
flag = 0  
i = 0  
for key in vul:  
    #print vul[key][0]  
    print u"正在写入%s的数据"%key  
    for n in range(len(vul[key])):  
        #print vul[key][n]  
        j = 0  
        for val in vul[key][n]:  
            table.write(i+1,j+1,vul[key][n][val])  
            table.write(i+1,0,key)  
  
            if flag == 0:  
                table.write(0,j+1,val)  
                if n != 0:  
                    flag = 1  
            j += 1  
        i += 1  
    print u"完成写入%s的数据"%key  
  
  
gk.save("gk.xls")  
  
fp.close()  
print u"完成json文件写入excel任务"  