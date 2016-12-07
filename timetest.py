#! /usr/bin/env python
# -*- coding=utf-8 -*-

import os
import sys
import re
import datetime

filename = "./4903_1.txt"
localpath = ""
timelist = []
calc_count = 0

def doCheck():
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        m = re.search(r'^\d+.*\s{1}:', line)
        #print m.group()
        n = m.group().rstrip().split(":")
        #print n
        timelist.append(n)
    #print timelist
    #print len(timelist)
    while calc_count < len(timelist):
        #print 'count is '  + str(calc_count)
        if calc_count == 0:
            #print 'First time, not calc'
            calc_count = calc_count + 1
        else:
            #print timelist[calc_count - 1]
            last_time_param = list(map(int, timelist[calc_count - 1][0:6]))
            #print 'last_time_param is %s' %last_time_param
            #last_time = datetime.datetime(int(timelist[calc_count - 1][0]), int(timelist[calc_count - 1][1]), int(timelist[calc_count - 1][2]), int(timelist[calc_count - 1][3]), int(timelist[calc_count - 1][4]), int(timelist[calc_count - 1][5]))
            last_time = datetime.datetime(*last_time_param)
            #print last_time
            current_time_param = list(map(int, timelist[calc_count][0:6]))
            #print current_time_param
            #current_time = datetime.datetime(int(timelist[calc_count][0]), int(timelist[calc_count][1]), int(timelist[calc_count][2]),int(timelist[calc_count][3]), int(timelist[calc_count][4]), int(timelist[calc_count][5]))
            current_time = datetime.datetime(*current_time_param)
            #print current_time
            calc_count = calc_count + 1
            elapsed = current_time - last_time
            if elapsed > datetime.timedelta(seconds=10):
                print 'find it! index is ' + str(calc_count)


if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print 'Usage:'
        print 'python timetest.py your_record.txt'
        exit()
    else:
        localpath = sys.argv[0]
        filename = sys.argv[1]

    if(not os.path.exists(filename)):
        print 'Cann\'t find the record file! %s' %filename
        exit()
    else:
        print 'local path is %s, record file name is %s' %(localpath, filename)
        #doCheck()

    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        m = re.search(r'^\d+.*\s{1}:', line)
        #print m.group()
        n = m.group().rstrip().split(":")
        #print n
        timelist.append(n)
    #print timelist
    #print len(timelist)
    while calc_count < len(timelist):
        #print 'count is '  + str(calc_count)
        if calc_count == 0:
            #print 'First time, not calc'
            calc_count = calc_count + 1
        else:
            #print timelist[calc_count - 1]
            last_time_param = list(map(int, timelist[calc_count - 1][0:6]))
            #print 'last_time_param is %s' %last_time_param
            #last_time = datetime.datetime(int(timelist[calc_count - 1][0]), int(timelist[calc_count - 1][1]), int(timelist[calc_count - 1][2]), int(timelist[calc_count - 1][3]), int(timelist[calc_count - 1][4]), int(timelist[calc_count - 1][5]))
            last_time = datetime.datetime(*last_time_param)
            #print last_time
            current_time_param = list(map(int, timelist[calc_count][0:6]))
            #print current_time_param
            #current_time = datetime.datetime(int(timelist[calc_count][0]), int(timelist[calc_count][1]), int(timelist[calc_count][2]),int(timelist[calc_count][3]), int(timelist[calc_count][4]), int(timelist[calc_count][5]))
            current_time = datetime.datetime(*current_time_param)
            #print current_time
            calc_count = calc_count + 1
            elapsed = current_time - last_time
            if elapsed > datetime.timedelta(seconds=10):
                print 'find it! index is ' + str(calc_count)
