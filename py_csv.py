# -*- coding: utf-8 -*-
import sys,os
import csv
import MySQLdb
os.chdir("/home/yutuo/downloads/teacherdata/股票贴吧数据/所有股票交易数据下载版/所有（3000）股票交易数据下载版""")
conn = MySQLdb.Connect(
    host='127.0.0.1',
    port = 3306,
    user ='root',
    passwd='root',
    db='stock',
    charset='utf8',
    use_unicode=True
)
curdor = conn.cursor()
conn.autocommit(False)
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
    sql_insert = "insert into stock(stock_id,stock_name) VALUE (%s,%s)"
    try:
        curdor.execute(sql_insert,[ins_id,ins_name])
        conn.commit()
    except Exception as e:
        print e
        conn.rollback()
    stock_csv.close()

for num in range(999999):
    num_filename = str(num).zfill(6) + ".csv"
    if (os.path.exists(num_filename)):
        read_name(num)
curdor.close()