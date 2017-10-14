# -*- coding: utf-8 -*-
import sys,os
import csv
import MySQLdb
os.chdir("/home/yutuo/downloads/teacherdata/股票贴吧数据/所有股票交易数据下载版/所有（3000）股票交易数据下载版""")

def read_name(num):
    ins_id = str(num).zfill(6)
    filename = str(num).zfill(6) + ".csv"
    stock_csv = open(filename, "rb+")
    read_stock_csv = csv.reader(stock_csv)
    i=0
    for eachline in read_stock_csv:
        i =i+1;
        if(i==3):
            ins_name = eachline[2].decode(encoding='GB18030')
            break
    print ins_id ,ins_name

for num in range(3):
    num_filename = str(num).zfill(6) + ".csv"
    if (os.path.exists(num_filename)):
        read_name(num)
