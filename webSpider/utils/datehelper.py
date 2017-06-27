#-*-coding:utf-8-*-
import time

__author__ = 'huligong'

def now_date():
    '''2012-09-09'''
    return time.strftime("%Y-%m-%d")

def now_time():
    '''22:43:42'''
    return time.strftime("%H:%M:%S")

def now_datetime():
    '''2012-09-09 22:43:42'''
    return time.strftime("%Y-%m-%d %H:%M:%S")

def time_str():
    '''20120909224342'''
    return time.strftime("%Y%m%d%H%M%S")

def time_str2():
    '''2012_09_09_22_44_56'''
    return time.strftime("%Y_%m_%d_%H_%M_%S")

def main():
    print now_date()
    print now_time()
    print now_datetime()
    print time_str()
    print time_str2()

if __name__ == '__main__':
    main()
