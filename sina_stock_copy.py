# -*- coding: utf-8 -*-
import sys,os
import csv
import MySQLdb
import re
import shutil
import threading
import  datetime
import multiprocessing
os.chdir("/home/yutuo/downloads/teacherdata/股票贴吧数据/新浪股吧/")
def creat_table(stock_id):
    post_name =str(stock_id)+"_1_post"
    reply_name =str(stock_id)+"_1_reply"
    creat_reply = "create table if not exists %s"% reply_name + "(reply_id int unsigned auto_increment primary key,昵称 varchar(30),时间 varchar(30),内容 text,post_id int unsigned)"
    creat_post = "create table if not exists %s" % post_name + "(post_id int unsigned auto_increment primary key,访问 int(7),回复 int(5),昵称 varchar(30),时间 varchar(30),主题 varchar(50),内容 text)"
    foreign_key ="alter table %s"% reply_name +" add foreign key(post_id) references %s"% post_name+"(post_id)"
    try:
        curdor.execute(creat_post)
        curdor.execute(creat_reply)
        curdor.execute(foreign_key)
        conn.commit()
    except Exception as e:
        print e
        conn.rollback()


def input_txt(post_name,reply_name,filename_txt):
    allLines = []
    with open(filename_txt,'r')as fp:
        allLines = fp.readlines()
    line_2 = allLines[1].decode(encoding='gbk')    # 回复
    totalen = len(allLines)
    if int(line_2[3:-1]) == 0:
        sql_insert = "insert into %s"% post_name +"(访问,回复,昵称,时间,主题,内容) VALUE (%s,%s,%s,%s,%s,%s)"
        try:
            line_1 = allLines[0].decode(encoding='gbk')  # 访问
            line_6 = allLines[6].decode(encoding='gbk')
            line_3 = allLines[2].decode(encoding='gbk')  # 昵称
            line_4 = allLines[3].decode(encoding='gbk')  # 时间
            line_5 = allLines[4].decode(encoding='gbk')  # 主题
            curdor.execute(sql_insert,
                           [line_1[3:-1],line_2[3:-1],line_3[3:-1],line_4[3:-1],line_5[3:-1],line_6[3:-1]])
            conn.commit()
        except Exception as e:
            #print e
            conn.rollback()
        fp.close()
    else:
        sql_max_id = "select max(post_id) from %s"% post_name
        sql_insert_post = "insert into %s"% post_name+"(访问,回复,昵称,时间,主题,内容) VALUE (%s,%s,%s,%s,%s,%s)"
        sql_insert_reply = "insert into %s"% reply_name+"(昵称,时间,内容,post_id) VALUE (%s,%s,%s,%s)"
        try:
            line_1 = allLines[0].decode(encoding='gbk')  # 访问
            line_6 = allLines[6].decode(encoding='gbk')
            line_3 = allLines[2].decode(encoding='gbk')  # 昵称
            line_4 = allLines[3].decode(encoding='gbk')  # 时间
            line_5 = allLines[4].decode(encoding='gbk')  # 主题
            curdor.execute(sql_insert_post ,
                           [line_1[3:-1], line_2[3:-1], line_3[3:-1], line_4[3:-1], line_5[3:-1], line_6[3:-1]])
            conn.commit()
        except Exception as e:
            #print e
            conn.rollback()
        curdor.execute(sql_max_id)
        max_id = curdor.fetchone()
        for i in range(0,int(line_2[3:-1])):
            try:
                w = allLines[totalen - (i + 1) * 5].decode(encoding='gbk')
                y = allLines[totalen - (i + 1) * 5 + 1].decode(encoding='gbk')
                t = allLines[totalen - (i + 1) * 5 + 2].decode(encoding='gbk')
                curdor.execute(sql_insert_reply,
                               [w[3:-1], t[3:-1], y[3:-1], max_id])
                conn.commit()
            except Exception as e:
                #print e
                conn.rollback()
        fp.close()
threads = []
conn = MySQLdb.Connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='root',
            db='stock',
            charset='utf8',
            use_unicode=True
        )
curdor = conn.cursor()
conn.autocommit(False)
start = datetime.datetime.now()
for num in range(418, 430):
    filename = "/home/yutuo/downloads/teacherdata/股票贴吧数据/新浪股吧/" + str(num).zfill(6)
    if os.path.exists(filename):
        post_name = str(num).zfill(6) + "_1_post"
        reply_name = str(num).zfill(6) + "_1_reply"
        print "doing:", filename
        creat_table(str(num).zfill(6))
        for i in range(700, 750):  # 计算每只股票有多少个txt
            while threads and len(threads) == 8:
                print "--------------------------"
                for thread in threads:
                    if not thread.is_alive():
                        threads.remove(thread)
            # filename_txt = os.path.join(filename, i)
            filename_txt = filename + "/" + str(i) + ".txt"
            input_txt(post_name, reply_name, filename_txt)
            thread = multiprocessing.Process(target=input_txt(post_name,reply_name,filename_txt))
            thread.start()
            threads.append(thread)

        end = datetime.datetime.now()
        print str(num).zfill(6), "using time:", (end - start)


curdor.close()
conn.close()