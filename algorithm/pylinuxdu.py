#!/usr/bin/python
#*-*coding:utf8*-*
import sys
import os
from optparse import OptionParser
#使用选项帮助信息可以使用中文
reload(sys)
sys.setdefaultencoding("utf-8")
#定义选项和帮助信息
usage = sys.argv[0] + " [选项]... [对象]..."
parser = OptionParser(usage)
parser.add_option("-s", 
         dest="sum",
         action="store_true",
         default=False,
         help="统计指定对象的的大小总和")
parser.add_option("-a",
         dest="autoDisplay",
         action="store_true",
         default=False,
         help="根据大小自动显示 k,KB,MB,GB 等单位")
options, args = parser.parse_args()
#判断文件或目录是否存在
def noFile(i):
  if not os.path.exists(i):
    sys.stderr.write(i + "\tis not exists\n")
    exit(1)
sum = 0
for i in args:
  noFile(i)
  if os.path.isfile(i):
    size = os.path.getsize(i)
    sum += size
    print("%d\t%s" %(size, i))
  if os.path.isdir(i):
    dir = os.walk(i)
    for x, y, z in dir:
      size = os.path.getsize(x)  #对目录本身进行大小统计，和du统计结果有点不太一样
      sum += size
      if options.sum:
        pass
      else:
        print("%d\t%s" %(size, x))
      for f in z:
        size = os.path.getsize(os.path.join(x, f))  #对目录里面文件进行大小统计
        sum += size
        if options.sum:
          pass
        else:
          print("%d\t%s" %(size, os.path.join(x, f)))
    """如果加上-s选项，这里就输入总的大小"""
    if options.sum:    
      print("%d\t%s" %(sum, i))