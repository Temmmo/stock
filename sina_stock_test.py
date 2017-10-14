# -*- coding: utf-8 -*-
import sys,os
import csv
import MySQLdb
import re
import shutil
import threading
import  datetime
import multiprocessing
conn ={}
curdor={}
def stock_I(num):

    filename = "/home/yutuo/data/东方财富股吧/" + str(num).zfill(6)
    if os.path.exists(filename):
        os.chdir("/home/yutuo/data/东方财富股吧/" + str(num).zfill(6))
        print "file exits"
        filename_txt = "/home/yutuo/data/东方财富股吧/" + str(num).zfill(6) + "/2.txt"
        r = 0
        with open(filename_txt, 'r')as fp:
            allLines = fp.readlines()
            print "file lines count:", len(allLines)
        visit_index = re.compile(r'^访问')
        visit = (allLines[r + 0].decode('gbk')).encode('utf-8')
        while str(re.match(visit_index, visit)) == 'None':
            r = r + 1
            visit = (allLines[r + 0].decode('gbk')).encode('utf-8')
        line_2 = allLines[r + 1].decode(encoding='gbk')  # 回复
        print "gg",int(line_2[3:-1])
        if 0 == (int(line_2[3:-1]) != 0):
            print line_2
        for i in range(0, int(line_2[3:-1])): # 处理回复
            w = allLines[r + 12 + i * 5].decode(encoding='gbk')  # 昵称
            y = allLines[r + 13 + i * 5].decode(encoding='gbk')  # 内容
            t = (allLines[r + 14 + i * 5].decode('gbk')).encode('utf-8')  # 时间
            time_index = re.compile(r'^time')
            while str(re.match(time_index, t)) == 'None':
                y = y + allLines[r + 14 + i * 5].decode(encoding='gbk')
                r = r + 1
                t = (allLines[r + 14 + i * 5].decode('gbk')).encode('utf-8')
            t = allLines[r + 14 + i * 5].decode(encoding='gbk')  # shijian
            print w
            print y
            print t
if __name__ =="__main__":
    stock_I(4)