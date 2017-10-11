# -*- coding: utf-8 -*-
import sys,os
import csv
import MySQLdb
import re
import shutil
import threading
import  datetime
import multiprocessing
os.chdir("/home/yutuo/stockdata/doc")
num =600075
os.chdir("/home/yutuo/stockdata/doc/" + str(num).zfill(6))
allLines = []
#try:
    #os.system('cat 1.txt 25.txt>file_big.txt')
#except Exception as e:
    #print e
file_big ="file_big.txt"
with open(file_big, 'r')as fp:
    allLines = fp.readlines()
print len(allLines)
count_index =0
num =0
while num < len(allLines) and count_index <630:
    count_index =count_index +1
    visit_index = re.compile(r'^访问')
    line_2 = (allLines[num + 0].decode('gbk')).encode('utf-8')
    while str(re.match(visit_index, line_2)) == 'None':
        num = num + 1
        line_2 = (allLines[num + 0].decode('gbk')).encode('utf-8')
    line_2 =allLines[num+1].decode(encoding='gbk')
    print "-------",count_index
    if 0 == (int(line_2[3:-1]) != 0):          # 判断是否有回复
        #print allLines[num+0].decode(encoding='gbk')  # 访问
        #print allLines[num+6].decode(encoding='gbk')
        #print allLines[num+2].decode(encoding='gbk')  # 昵称
        #print allLines[num+3].decode(encoding='gbk')  # 时间
        #print allLines[num+4].decode(encoding='gbk')  # 主题
        num =num +10
    else:
        #print allLines[num+0].decode(encoding='gbk')  # 访问
        #print allLines[num+6].decode(encoding='gbk')
        #print allLines[num+2].decode(encoding='gbk')  # 昵称
        #print allLines[num+3].decode(encoding='gbk')  # 时间
        #print allLines[num+4].decode(encoding='gbk')  # 主题
        for i in range(0, int(line_2[3:-1])):
                print "*******************"
                w=allLines[num + 12 + i * 5].decode(encoding='gbk')
                y= allLines[num + 13 + i * 5].decode(encoding='gbk')
                t= (allLines[num + 14 + i * 5].decode('gbk')).encode('utf-8')
                time_index = re.compile(r'^时间')
                while str(re.match(time_index, t)) == 'None':
                    y = y+allLines[num + 14 + i * 5].decode(encoding='gbk')
                    num = num + 1
                    t = (allLines[num + 14 + i * 5].decode('gbk')).encode('utf-8')
                #print w
                print y[3:-1]
                print len(y)
                #print allLines[num + 14 + i * 5].decode(encoding='gbk')
        num = num + 12+5*int(line_2[3:-1])
