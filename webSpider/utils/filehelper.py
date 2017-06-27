#-*-coding:utf-8-*-
import time
from utils import datehelper, dirhelper

__author__ = 'huligong'

import csv

file_root = dirhelper.get_file_folder()

def write_to_csv(title_list=[],data_list=[],file_name=None,file_path=None):
    '''data write to csv file'''
    real_path = ''
    if file_path:
        real_path = file_path
    else:
        real_path = file_root
    if file_name:
        real_path +=  file_name
    else:
        real_path +=  datehelper.time_str2()+'.csv'
    csvfile = file(real_path, 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(title_list)
    writer.writerows(data_list)
    csvfile.close()
    return real_path

def read_csv(file_path):
    csvfile = file(file_path, 'rb')
    reader = csv.reader(csvfile)
    for line in reader:
        print line
    csvfile.close()


def main():
    starttime = time.clock()

    title_list = ['姓名', '年龄', '电话']
    data_list = [
        ('小河', '25', '1234567'),
        ('小芳', '18', '789456')
    ]
    filepath =  write_to_csv(title_list,data_list)
    print filepath
    read_csv(filepath)
    endtime = time.clock()
    print '[All Task Finished in '+str(endtime-starttime)+'s]'


if __name__ == '__main__':
    main()