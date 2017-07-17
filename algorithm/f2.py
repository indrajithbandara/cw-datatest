# -*- coding: utf-8 -*-
import sys
sys.path.append('D:/360data/重要数据/桌面')
import f1
F1 = f1.sckt()
F1.run_server()
Open = []
for i in range(0, 99):
    Open.append(F1.run_client())
    print(Open)